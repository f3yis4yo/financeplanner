from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve database credentials from environment variables
DB_USER  = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("BD_NAME")


# Construct the database connection URL
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
# Create the SQLAlchemy engine, which is the entry point to the database
engine = create_engine(DATABASE_URL, echo=True)  # echo=True will log SQL statements
# Create a base for declarative models, which will be used to define database tables as Python classes
base = declarative_base()

# Define the 'user' model, which maps to the 'user_a' table in the database
class user(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    confirm_password = Column(String(100), nullable=False)
    security_question = Column(String(100), nullable=False)
    security_answer = Column(String(100), nullable=False)
    terms_accepted = Column(String(100), nullable=False)
    updates_subscribed = Column(String(100), nullable=False)

 # Constructor for the 'user' class
    def __init__(self, fullname, email, phone, password, confirm_password, security_question, security_answer, terms_accepted, updates_subscribed):
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.password = password
        self.confirm_password = confirm_password
        self.security_question = security_question
        self.security_answer = security_answer
        self.terms_accepted = terms_accepted
        self.updates_subscribed = updates_subscribed

# Create all the tables defined in the declarative base in the database
base.metadata.create_all(engine)

# Create a sessionmaker, which is a factory for creating database sessions
session = sessionmaker(bind=engine)
# Create an active database session
sessionActive = session()