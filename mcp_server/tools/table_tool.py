from services.metadata_service import MetadataService

metadata_service = MetadataService()

def register(mcp):
    @mcp.tool(name="list_tables",description="List all tables in a schema.")
    def list_tables(schema:str):
        """
        List all tables belonging to the provided schema.

        Args:
            schema (str): PostgreSQL schema name.

        Returns:
            list: List of tables.
        """

        tables = metadata_service.list_tables(schema)

        return [
            table.model_dump()
            for table in tables
        ]
        
    