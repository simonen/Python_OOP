from abc import ABC, abstractmethod
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    FISH_TYPES = []

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: list[BaseDecoration] = []
        self.fish: list[BaseFish] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.split():
            raise ValueError("Aquarium name cannot be an empty string.")

        self._name = value

    def calculate_comfort(self):
        return sum(x.comfort for x in self.decorations)

    def add_fish(self, fish: BaseFish) -> str:
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish) -> None:
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration) -> None:
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_list = [x.name for x in self.fish] if self.fish else ["none"]
        res = ([f"{self.name}:",
                f"Fish: {' '.join(fish_list)}"] +
               [f"Decorations: {len(self.decorations)}"] +
               [f"Comfort: {self.calculate_comfort()}"])
        return "\n".join(res)
