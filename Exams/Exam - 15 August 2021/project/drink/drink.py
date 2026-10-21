from abc import ABC,abstractmethod


class Drink(ABC):
    def __init__(self, name: str, portion: float, price: float, brand: str) -> None:
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    def __repr__(self) -> str:
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.split():
            raise ValueError("Name cannot be empty string or white space!")

        self._name = value

    @property
    def portion(self):
        return self._portion

    @portion.setter
    def portion(self, value: float):
        if value <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")

        self._portion = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value: str):
        if not value.split():
            raise ValueError("Brand cannot be empty string or white space!")

        self._brand = value