from enum import Enum


class EntityType(str, Enum):
    DATASET = "DATASET"
    DISCUSSION = "DISCUSSION"
    PROCESS = "PROCESS"
    PROJECT = "PROJECT"
    REFERENCE = "REFERENCE"
    SAMPLE = "SAMPLE"
    SHARE = "SHARE"
    SHEET = "SHEET"
    TAG = "TAG"
    UNKNOWN = "UNKNOWN"
    USER = "USER"
    WORKSPACE = "WORKSPACE"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, number):
        return cls(cls.UNKNOWN)
