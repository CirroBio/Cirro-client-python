from enum import Enum


class AppClientType(str, Enum):
    CONFIDENTIAL_CLIENT = "CONFIDENTIAL_CLIENT"
    PUBLIC_CLIENT = "PUBLIC_CLIENT"
    UNKNOWN = "UNKNOWN"
    """ This is a fallback value for when the value is not known, do not use this value when making requests """

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, number):
        return cls(cls.UNKNOWN)
