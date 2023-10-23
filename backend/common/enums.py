from enum import Enum


class ChoicesEnum(Enum):
    @classmethod
    def verbs(cls) -> dict:
        ...

    @classmethod
    def choices(cls):
        return tuple((i.name, i.verb) for i in cls)

    @property
    def verb(self):
        return self.__class__.verbs()[self]

    @classmethod
    def names(cls) -> list:
        return [i.name for i in cls]
