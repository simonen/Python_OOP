from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        ...

class Chicken(Animal):
    def make_sound(self):
        return 'Kur-kur'

class Cat(Animal):
    def make_sound(self):
        return 'meow'

class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


def animal_sound(animals: List[Animal]) -> None:
    for animal in animals:
        animal.make_sound()


cat = Cat('cat')
dog = Dog('dog')
animals = [cat, dog]
animal_sound(animals)
print(cat.make_sound())
## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
