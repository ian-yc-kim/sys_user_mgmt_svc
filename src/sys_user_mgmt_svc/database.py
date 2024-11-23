from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from .config import settings


# Create the SQLAlchemy engine using the DATABASE_URL from settings
engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG)

# Scoped session to ensure thread safety
SessionLocal = scoped_session(sessionmaker(bind=engine))

# Base class for declarative models
Base = declarative_base()
