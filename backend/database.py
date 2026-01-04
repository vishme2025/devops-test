from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()

def get_database_url():
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL is not set")
    return url

def get_engine():
    return create_engine(get_database_url())

SessionLocal = sessionmaker(autocommit=False, autoflush=False)