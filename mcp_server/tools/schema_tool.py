from services.metadata_service import MetadataService

metadata_service = MetadataService()

def register(mcp):
    @mcp.tool(name="list_schemas",description="List all schemas in the database.")
    def list_schemas():
        schemas=metadata_service.list_schemas()
        return [schema.model_dump() for schema in schemas]