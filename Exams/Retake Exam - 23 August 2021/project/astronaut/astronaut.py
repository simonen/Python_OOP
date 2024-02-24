from abc import ABC, abstractmethod


class Astronaut(ABC):

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    @abstractmethod
    def breathe(self):
        pass

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __repr__(self) -> str:
        return f"Type: {self.__class__.__name__}, {self.name}, {self.oxygen}, {self.backpack}"

    def details(self):
        return [f"Name: {self.name}", f"Oxygen: {self.oxygen}",
                f"Backpack items: {', '.join(self.backpack) if self.backpack else 'none'}"]

