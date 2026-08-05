import os
import sys

# Add project root to sys.path when running server.py directly from inside the package folder.
if __package__ is None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

from fastmcp import FastMCP

from mcp_server.tools.schema_tool import register as register_schema_tools
from mcp_server.tools.table_tool import register as register_table_tools
from mcp_server.tools.columns_tool import register as register_column_tools
from mcp_server.tools.sample_tool import register as register_sample_tools
from mcp_server.tools.query_tool import register as register_query_tools

mcp = FastMCP(
    name="mcp_server",
    version="0.1.0",
)

register_schema_tools(mcp)
register_table_tools(mcp)
register_column_tools(mcp)
register_sample_tools(mcp)
register_query_tools(mcp)




if __name__ == "__main__":
    mcp.run()
