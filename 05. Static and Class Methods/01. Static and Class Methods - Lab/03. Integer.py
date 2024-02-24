import math


class Integer:

    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"

        return cls(math.floor(float_value))

    @classmethod
    def from_roman(cls, value: str):
        romans = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XIX': 19}
        if value in romans:
            return cls(romans[value])

    @classmethod
    def from_string(cls, value: str):
        try:
            value = int(str(value))
            return cls(value)
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)
second_num = Integer.from_roman("IV")
print(second_num.value)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))