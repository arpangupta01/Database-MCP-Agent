from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import get_settings
from Utils.logger import logger


settings = get_settings()
engine = create_engine(settings.database_url,pool_pre_ping=True,pool_size=10,max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Provides a database session for interacting with the database.
    
    Yields:
        Session: A SQLAlchemy session for database operations.
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database session error: {e}")
        raise
    finally:
        db.close()
