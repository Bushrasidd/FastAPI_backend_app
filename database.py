import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

if DATABASE_URL is not None:
    print(f"Database found:{DATABASE_URL}")
else:
    print("DATABASE_URL not found in environment variables.")

DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()