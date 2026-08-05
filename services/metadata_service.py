from database.metadata_repositories import MetadataRepository


class MetadataService:

    def __init__(self):
        self.repository = MetadataRepository()

    def list_schemas(self):

        return self.repository.get_schemas()

    def list_tables(
        self,
        schema: str,
    ):

        schemas = self.repository.get_schemas()

        schema_names = [
            s.name
            for s in schemas
        ]

        if schema not in schema_names:

            raise ValueError(
                f"Schema '{schema}' does not exist."
            )

        return self.repository.get_tables(schema)

    def list_columns(
        self,
        schema,
        table,
    ):

        return self.repository.get_columns(
            schema,
            table,
        )

    def foreign_keys(self):

        return self.repository.get_foreign_keys()

    def sample_rows(
        self,
        schema,
        table,
        limit: int = 5,
    ):

         return self.repository.get_sample_rows(
        schema=schema,
        table=table,
        limit=limit,
    )