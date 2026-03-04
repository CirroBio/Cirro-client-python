from enum import Enum


class AppType(str, Enum):
    MACHINE_TO_MACHINE = "MACHINE_TO_MACHINE"
    PUBLIC_APP = "PUBLIC_APP"
    TRADITIONAL = "TRADITIONAL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, number):
        return cls(cls.UNKNOWN)
