import sqlparse


class SQLValidator:

    FORBIDDEN = {
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "CREATE",
        "TRUNCATE",
        "GRANT",
        "REVOKE",
    }

    @classmethod
    def validate(cls, sql):

        parsed = sqlparse.parse(sql)

        if not parsed:
            raise ValueError("Invalid SQL")

        statement = parsed[0]

        tokens = {
            token.value.upper()
            for token in statement.tokens
        }

        forbidden = tokens.intersection(
            cls.FORBIDDEN
        )

        if forbidden:
            raise PermissionError(
                f"Forbidden SQL: {forbidden}"
            )

        return True