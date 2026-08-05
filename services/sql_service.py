from tools.sql_executor import SQLExecutor


class SQLService:

    def __init__(self):

        self.executor = SQLExecutor()

    def run_query(
        self,
        sql: str,
    ):

        return self.executor.execute(sql)