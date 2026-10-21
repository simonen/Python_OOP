from abc import ABC, abstractmethod


class BakedFood(ABC):
    def __init__(self, name: str, portion: float, price) -> None:
        self.name = name
        self.portion = portion
        self.price = price

    def __repr__(self) -> str:
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value.split():
            raise ValueError("Name cannot be empty string or white space!")

        self._name = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Price cannot be less than or equal to zero!")

        self._price = value
