from abc import ABC, abstractmethod
from project.animals.animal import Animal, Mammal
from project.food import Food, Vegetable, Fruit, Meat, Seed


mice_food = ['Vegetable', 'Fruit']
cat_food = ['Vegetable', 'Meat']


class Mouse(Mammal):
    @staticmethod
    def make_sound() -> str:
        return "Squeak"

    @property
    def foods(self) -> list:
        return [Vegetable, Fruit]

    @property
    def weight_gain(self) -> float:
        return 0.1


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def foods(self) -> list:
        return [Meat]

    @property
    def weight_gain(self) -> float:
        return 0.4


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def foods(self) -> list:
        return [Vegetable, Meat]

    @property
    def weight_gain(self) -> float:
        return 0.30


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def foods(self) -> list:
        return [Meat]

    @property
    def weight_gain(self) -> float:
        return 1.00
