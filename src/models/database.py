from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the SQLite database URL
DATABASE_URL = "sqlite:///./financeplanner.db"  # Creates a file named financeplanner.db in the current directory
engine = create_engine(DATABASE_URL, echo=True)
base = declarative_base()

class user(base):
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

    def __init__(self, fullname, email, phone, password, confirm_password, security_question, security_answer, terms_accepted, updates_subscribed):
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.password = password
        self.security_question = security_question
        self.security_answer = security_answer
        self.terms_accepted = terms_accepted
        self.updates_subscribed = updates_subscribed

# Create all the tables defined in the declarative base in the database if they don't exist
base.metadata.create_all(engine)

# Create a sessionmaker, which is a factory for creating database sessions
Session = sessionmaker(bind=engine)

# Function to get a database session
def get_session():
    return Session()

# Example of how to use the session (you might want to move this to where you need database interaction)
if __name__ == "__main__":
    session = get_session()
    try:
        # Example: Adding a new user
        new_user = user(
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
        users = session.query(user).all()
        for u in users:
            print(f"ID: {u.id}, Fullname: {u.fullname}, Email: {u.email}")

    except Exception as e:
        session.rollback()
        print(f"❌ An error occurred: {e}")
    finally:
        session.close()