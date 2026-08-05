"""
Column related MCP tools.

This module exposes tools that allow the LLM to discover
the columns of a table before generating SQL.
"""

from services.metadata_service import MetadataService

metadata_service = MetadataService()


def register(mcp):
    """
    Register column related tools.
    """

    @mcp.tool(
        name="list_columns",
        description="Returns all columns for a given schema and table."
    )
    def list_columns(schema: str, table: str) -> list:
        """
        Get columns of a PostgreSQL table.

        Args:
            schema: PostgreSQL schema name.
            table: Table name.

        Returns:
            List of column metadata.
        """

        columns = metadata_service.list_columns(
            schema=schema,
            table=table
        )

        return [
            column.model_dump()
            for column in columns
        ]