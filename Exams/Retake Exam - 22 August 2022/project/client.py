from project.meals.meal import Meal


class Client:
    def __init__(self, phone_number: str) -> None:
        self.phone_number = phone_number
        self.shopping_cart: list[Meal] = []
        self.bill: float = 0.0

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if (any(not n.isdigit() for n in value)
                or len(value) != 10
                or value[0] != "0"):
            raise ValueError("Invalid phone number!")

        self._phone_number = value
