from abc import ABC, abstractmethod
from typing import ClassVar


class Meal(ABC):
    # _QUANTITY: ClassVar[int]
    _QUANTITY = {"Starter": 60, "MainDish": 50, "Dessert": 30}
    _default_quantity: int | None = None

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        cls._default_quantity = Meal._QUANTITY[cls.__name__]
        print(cls.__dict__)

    def __init__(self, name: str, price: float, quantity: int | None = None) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity if quantity is not None else self._default_quantity

    @abstractmethod
    def details(self):
        ...

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.split():
            raise ValueError("Name cannot be an empty string!")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Invalid price!")

        self.__price = value