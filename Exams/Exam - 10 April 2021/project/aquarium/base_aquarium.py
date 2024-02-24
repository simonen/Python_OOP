from abc import ABC, abstractmethod
from typing import List
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish: BaseFish) -> str:
        if self.capacity >= len(self.fish) + 1:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

        return f"Not enough capacity."

    def remove_fish(self, fish: BaseFish) -> None:
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration) -> None:
        self.decorations.append(decoration)

    def feed(self) -> None:
        for fish in self.fish:
            fish.eat()

    def __str__(self) -> str:
        return f"{self.name}:" \
               f"\nFish: {' '.join([f.name for f in self.fish]) if self.fish else 'none'}" \
               f"\nDecorations: {len(self.decorations)}" \
               f"\nComfort: {self.calculate_comfort()}"
