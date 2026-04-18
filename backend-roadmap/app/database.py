from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/backend_db"

engine = create_engine(DATABASE_URL, client_encoding="utf8")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()