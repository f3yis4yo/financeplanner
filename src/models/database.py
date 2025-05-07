from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Date, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
import os
import sys

# Define a function to get the correct database URL for both development and PyInstaller
def get_database_url():
    if getattr(sys, 'frozen', False):
        # The application is frozen (packaged by PyInstaller)
        base_path = sys._MEIPASS
    else:
        # The application is running from source
        base_path = os.path.abspath(".")

    # Create the data directory if it doesn't exist
    data_dir = os.path.join(base_path, "data")
    os.makedirs(data_dir, exist_ok=True)

    database_path = os.path.join(data_dir, "financeplanner.db")
    return f"sqlite:///{database_path}"

# Define the SQLite database URL using the function
DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL, echo=False)  # Set echo=True for debugging SQL
base = declarative_base()

class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    security_question = Column(String(100), nullable=False)
    security_answer = Column(String(100), nullable=False)
    terms_accepted = Column(String(100), nullable=False)
    updates_subscribed = Column(String(100), nullable=False)

    expenses = relationship("Expense", back_populates="user")
    budgets = relationship("Budget", back_populates="user")

    def __init__(self, fullname, email, phone, password, confirm_password, security_question, security_answer, terms_accepted, updates_subscribed):
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.password = password
        self.security_question = security_question
        self.security_answer = security_answer
        self.terms_accepted = terms_accepted
        self.updates_subscribed = updates_subscribed

class Expense(base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    expense_name = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)
    notes = Column(String(200), nullable=True)
    created_at = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="expenses")

class Budget(base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    monthly_income = Column(Float, nullable=False)
    monthly_budget = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)

    user = relationship("User", back_populates="budgets")
    allocations = relationship("BudgetAllocation", back_populates="budget", cascade="all, delete-orphan")

class BudgetAllocation(base):
    __tablename__ = 'budget_allocations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    budget_id = Column(Integer, ForeignKey('budgets.id'), nullable=False)
    category = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)

    budget = relationship("Budget", back_populates="allocations")

# Create all the tables defined in the declarative base in the database if they don't exist
base.metadata.create_all(engine)

# Create a sessionmaker, which is a factory for creating database sessions
Session = sessionmaker(bind=engine)

# Helper functions
def get_session():
    return Session()

def get_current_budget(user_id):
    session = get_session()
    try:
        return (session.query(Budget)
                .filter(Budget.user_id == user_id)
                .order_by(Budget.start_date.desc())
                .first())
    finally:
        session.close()

def update_or_create_budget(session, user_id, monthly_income, monthly_budget, allocations):
    try:
        # Clear all previous expenses for the user
        clear_user_expenses(session, user_id)

        # Obtain the most recent budget that the user has input
        existing_budget = (session.query(Budget)
                         .filter(Budget.user_id == user_id)
                         .order_by(Budget.start_date.desc())
                         .first())
        if existing_budget:
            # Update the current budget
            existing_budget.monthly_income = monthly_income
            existing_budget.monthly_budget = monthly_budget

            # Clear current allocations
            session.query(BudgetAllocation).filter(
                BudgetAllocation.budget_id == existing_budget.id
            ).delete()

            # Add new allocations
            for category, amount in allocations.items():
                allocation = BudgetAllocation(
                    budget_id=existing_budget.id,
                    category=category,
                    amount=amount
                )
                session.add(allocation)

            budget_id = existing_budget.id
        else:
            # Create new budget
            new_budget = Budget(
                user_id=user_id,
                monthly_income=monthly_income,
                monthly_budget=monthly_budget,
                start_date=datetime.now().date()
            )
            session.add(new_budget)
            session.flush()  # ensure the new budget obtains an ID before use

            # Create allocations
            for category, amount in allocations.items():
                allocation = BudgetAllocation(
                    budget_id=new_budget.id,
                    category=category,
                    amount=amount
                )
                session.add(allocation)
            budget_id = new_budget.id

        session.commit()
        return budget_id
    except:
        session.rollback()
        raise

def clear_user_expenses(session, user_id):
    try:
        # Clear all expenses for user once new budget is set
        session.query(Expense).filter(Expense.user_id == user_id).delete()
        session.commit()
    except Exception as e:
        session.rollback()
        raise

def get_user_expenses(user_id, limit=None):
    session = get_session()
    try:
        query = (session.query(Expense)
                .filter(Expense.user_id == user_id)
                .order_by(Expense.date.desc()))
        if limit:
            query = query.limit(limit)
        return query.all()
    finally:
        session.close()

def get_total_expenses(user_id):
    session = get_session()
    try:
        result = session.query(func.sum(Expense.amount))\
                .filter(Expense.user_id == user_id)\
                .scalar()
        return float(result) if result else 0.0
    finally:
        session.close()

def get_expenses_by_category(user_id):
    session = get_session()
    try:
        results = session.query(
            Expense.category,
            func.sum(Expense.amount).label('total')
        ).filter(Expense.user_id == user_id)\
         .group_by(Expense.category)\
         .all()
        return {cat: float(total) for cat, total in results}
    finally:
        session.close()

def get_monthly_expenses(user_id, year, month):
    session = get_session()
    try:
        start_date = datetime(year, month, 1).date()
        if month == 12:
            end_date = datetime(year + 1, 1, 1).date()
        else:
            end_date = datetime(year, month + 1, 1).date()

        return session.query(Expense)\
            .filter(Expense.user_id == user_id,
                   Expense.date >= start_date,
                   Expense.date < end_date)\
            .all()
    finally:
        session.close()

# Example of how to use the session
if __name__ == "__main__":
    session = get_session()
    try:
        # Example: Adding a new user
        new_user = User(
            fullname="Test User",
            email="test@example.com",
            phone="1234567890",
            password="password",
            confirm_password="password",
            security_question="What is your favorite color?",
            security_answer="blue",
            terms_accepted="True",
            updates_subscribed="False"
        )
        session.add(new_user)
        session.commit()
        print("✅ User added successfully.")

        # Example: Querying users
        users = session.query(User).all()
        for u in users:
            print(f"ID: {u.id}, Fullname: {u.fullname}, Email: {u.email}")

    except Exception as e:
        session.rollback()
        print(f"❌ An error occurred: {e}")
    finally:
        session.close()