from fastmcp import FastMCP
from database.metadata_repositories import MetadataRepository
import mcp_server
from tools.sql_executor import SQLExecutor

mcp = FastMCP(
    name="mcp_server",
    version="0.1.0",
)
repository = MetadataRepository()

executor = SQLExecutor()

@mcp.tool()
def list_schemas():
    return [
        schema.model_dump()
        for schema in repository.get_schemas()
    ]


@mcp.tool()
def list_tables(schema: str):
    return [
        table.model_dump()
        for table in repository.get_tables(schema)
    ]


@mcp.tool()
def list_columns(
    schema: str,
    table: str,
):
    return [
        column.model_dump()
        for column in repository.get_columns(
            schema,
            table,
        )
    ]


@mcp.tool()
def foreign_keys():
    return [
        key.model_dump()
        for key in repository.get_foreign_keys()
    ]


@mcp.tool()
def sample_rows(
    schema: str,
    table: str,
):
    return repository.get_sample_rows(
        schema,
        table,
    )


@mcp.tool()
def run_safe_query(sql: str):
    return executor.execute(sql)


if __name__ == "__main__":
    mcp.run()
