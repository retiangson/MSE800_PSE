from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# Create engine
engine = create_engine(DATABASE_URL, echo=False)

# Session factory
SessionLocal = sessionmaker(bind=engine)