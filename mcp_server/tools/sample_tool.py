"""
Sample row related MCP tools.

This tool helps the LLM understand the
actual data stored inside a table.
"""

from services.metadata_service import MetadataService

metadata_service = MetadataService()


def register(mcp):
    """
    Register sample row tool.
    """

    @mcp.tool(
        name="sample_rows",
        description=(
            "Returns a small number of sample rows from a table "
            "to help understand the data."
        ),
    )
    def sample_rows(
        schema: str,
        table: str,
        limit: int = 5,
    ) -> list[dict]:
        """
        Return sample rows from a table.

        Args:
            schema: PostgreSQL schema
            table: Table name
            limit: Number of rows (default 5)

        Returns:
            List of dictionaries
        """

        return metadata_service.sample_rows(
            schema=schema,
            table=table,
            limit=limit,
        )