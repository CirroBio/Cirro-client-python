from enum import Enum


class SemanticColumnType(str, Enum):
    CIRRO_DATASET = "CIRRO_DATASET"
    CIRRO_FILE = "CIRRO_FILE"
    CIRRO_FOLDER = "CIRRO_FOLDER"
    ENUM_MULTI = "ENUM_MULTI"
    ENUM_SINGLE = "ENUM_SINGLE"
    FOREIGN_KEY = "FOREIGN_KEY"
    STANDARD = "STANDARD"
    URL = "URL"
    UNKNOWN = "UNKNOWN"
    """ This is a fallback value for when the value is not known, do not use this value when making requests """

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, number):
        return cls(cls.UNKNOWN)
