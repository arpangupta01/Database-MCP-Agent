from pydantic import BaseModel



class SchemaInfo(BaseModel):
    name: str


class TableInfo(BaseModel):
    schema: str
    table: str


class ColumnInfo(BaseModel):
    schema: str
    table: str
    column: str
    datatype: str
    nullable: bool


class ForeignKeyInfo(BaseModel):
    table: str
    column: str
    referenced_table: str
    referenced_column: str