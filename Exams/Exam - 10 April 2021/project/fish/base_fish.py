from abc import ABC, abstractmethod


class BaseFish(ABC):
    def __init__(self, name: str, species: str, size: int, price: float) -> None:
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @abstractmethod
    def eat(self):
        ...

    @staticmethod
    def _is_valid(string: str):
        if not string.split():
            return False
        return True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not self._is_valid(value):
            raise ValueError("Fish name cannot be an empty string.")
        self._name = value

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value: str):
        if not self._is_valid(value):
            raise ValueError("Fish species cannot be an empty string.")
        self._species = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self._price = value
