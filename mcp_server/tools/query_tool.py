"""
SQL Query MCP Tool

This tool executes only safe SELECT queries.
"""

from services.sql_service import SQLService

sql_service = SQLService()


def register(mcp):
    """
    Register SQL execution tool.
    """

    @mcp.tool(
        name="run_safe_query",
        description=(
            "Execute a read-only SQL query on PostgreSQL "
            "and return the result."
        ),
    )
    def run_safe_query(sql: str) -> list[dict]:
        """
        Execute SQL after validation.

        Args:
            sql: Generated SQL query

        Returns:
            Query result as JSON
        """

        return sql_service.run_query(sql)