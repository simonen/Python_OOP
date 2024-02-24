from typing import List


class Animal:
    def __init__(self, species) -> None:
        self.species = species

    def get_species(self) -> str:
        return self.species

    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self) -> str:
        return 'meow'


class Dog(Animal):
    def make_sound(self) -> str:
        return 'woof-woof'


def animal_sound(animals: List[Animal]) -> None:
    for animal in animals:
        print(animal.make_sound())


cat = Cat('cat')
dog = Dog('dog')
animals = [cat, dog]
animal_sound(animals)
print(cat.make_sound())
## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
