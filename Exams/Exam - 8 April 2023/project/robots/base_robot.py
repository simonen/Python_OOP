from abc import ABC, abstractmethod


class BaseRobot(ABC):
    def __init__(self, name: str, kind: str, price: float, weight: int) -> None:
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @abstractmethod
    def eating(self):
        ...

    @staticmethod
    def is_valid(string: str) -> bool:
        if not string.split():
            return False
        return True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not self.is_valid(value):
            raise ValueError("Robot name cannot be empty!")
        self._name = value

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value: str):
        if not self.is_valid(value):
            raise ValueError("Robot kind cannot be empty!")
        self._kind = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")
        self._price = value

    def __repr__(self) -> str:
        return f"{self.name} {self.__class__.__name__} {self.kind}"