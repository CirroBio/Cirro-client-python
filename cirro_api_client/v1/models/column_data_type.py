from enum import Enum


class ColumnDataType(str, Enum):
    BIGINT = "BIGINT"
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    DOUBLE = "DOUBLE"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    STRING = "STRING"
    TIMESTAMP = "TIMESTAMP"
    UNKNOWN = "UNKNOWN"
    """ This is a fallback value for when the value is not known, do not use this value when making requests """

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, number):
        return cls(cls.UNKNOWN)
