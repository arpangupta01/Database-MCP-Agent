from sqlalchemy import text
from database.connections import SessionLocal, engine

from database.models import(
    ColumnInfo,
    ForeignKeyInfo,
    SchemaInfo,
    TableInfo
)

class MetadataRepository:
    def __init__(self):
        self.session = SessionLocal()
    
    def close(self):
        self.session.close()
        
        
def get_schemas(self):
    query = text("""
        SELECT schema_name
        FROM information_schema.schemata
        WHERE schema_name NOT IN (
            'pg_catalog',
            'information_schema'
        )
        ORDER BY schema_name;
    """)

    rows = self.session.execute(query)

    return [
        SchemaInfo(name=row.schema_name)
        for row in rows
    ]        

def get_tables(self, schema: str):
    query = text("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = :schema
        ORDER BY table_name;
    """)

    rows = self.session.execute(query, {"schema": schema})

    return [
        TableInfo(schema=schema, table=row.table_name)
        for row in rows
    ]
    
def get_columns(self,schema:str,table:str)->list[ColumnInfo]:
    query = text("""
        SELECT
            column_name,
            data_type,
            is_nullable
        FROM information_schema.columns
        WHERE table_schema=:schema
        AND table_name=:table
        ORDER BY ordinal_position;
    """)
    rows = self.session.execute(query, {"schema": schema, "table": table})
    return [
        ColumnInfo(
            schema=schema,
            table=table,
            column=row.column_name,
            datatype=row.data_type,
            nullable=row.is_nullable == "YES",
        )
        for row in rows
    ]
              