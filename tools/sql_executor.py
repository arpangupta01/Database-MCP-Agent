from sqlalchemy import text

from database.connections import SessionLocal
from tools.sql_validator import SQLValidator


class SQLExecutor:

    def execute(self, sql):

        SQLValidator.validate(sql)

        session = SessionLocal()

        try:

            rows = session.execute(text(sql))

            return [
                dict(row._mapping)
                for row in rows
            ]

        finally:
            session.close()