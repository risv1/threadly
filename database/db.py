from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from databases import Database
from dotenv import load_dotenv
from os import getenv

load_dotenv()

DATABASE_URL = getenv('DB_URL')

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def get_db():
    db = Database(DATABASE_URL)
    return db
