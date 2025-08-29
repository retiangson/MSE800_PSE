from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from infrastructure.config import DB_URL

Base = declarative_base()

def get_engine(db_url: str = None):
    if db_url is None:
        db_url = DB_URL
    return create_engine(db_url, echo=False, future=True)

def get_session_factory(engine=None):
    if engine is None:
        engine = get_engine()
    return scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False, future=True))
