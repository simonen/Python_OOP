from abc import ABC, abstractmethod
from project.animals.animal import Bird
from project.food import Food, Vegetable, Fruit, Meat, Seed


class Owl(Bird):

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"

    @property
    def foods(self) -> list:
        return [Meat]

    @property
    def weight_gain(self) -> float:
        return 0.25


class Hen(Bird):

    @staticmethod
    def make_sound() -> str:
        return "Cluck"

    @property
    def foods(self) -> list:
        return [Vegetable, Meat, Seed, Fruit]

    @property
    def weight_gain(self) -> float:
        return 0.35
