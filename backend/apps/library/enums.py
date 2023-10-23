from common.enums import ChoicesEnum

RATE_CHOICES = (
    (1, 'One'),
    (2, 'Two'),
    (3, 'Three'),
    (4, 'Four'),
    (5, 'Five'),
)


class RateChoices(int, ChoicesEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    @classmethod
    def verbs(cls) -> dict:
        return {
            cls.ONE: 1,
            cls.TWO: 2,
            cls.THREE: 3,
            cls.FOUR: 4,
            cls.FIVE: 5,
        }

