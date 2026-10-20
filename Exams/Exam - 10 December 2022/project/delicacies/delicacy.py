from abc import ABC, abstractmethod


class Delicacy(ABC):
    def __init__(self, name: str, portion: int, price: float) -> None:
        self.name = name
        self.portion = portion  # grams
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.split():
            raise ValueError("Name cannot be null or whitespace!")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0.0:
            raise ValueError("Price cannot be less or equal to zero!")
        self._price = value

    @abstractmethod
    def details(self):
        ...