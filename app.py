from sqlalchemy import text
from database.connections import get_db
from database.connections import engine

from Utils.logger import logger

def test_database_connection():
    try:
        with engine.connect() as db:
            # Execute a simple query to test the connection
            result = db.execute(text("SELECT version();"))
            if result.scalar():
                logger.info(f"Database connection successful. {result}")
            else:
                logger.error("Database connection failed.")
    except Exception as e:
        logger.error(f"Database connection error: {e}")

if __name__ == "__main__":
    test_database_connection()                    