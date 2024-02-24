from abc import ABC, abstractmethod
from project.animals.animal import Animal, Bird
from project.animals.birds import Owl, Hen
from project.animals.mammals import Dog, Mouse, Cat, Tiger
from project.food import Food, Vegetable, Fruit, Meat, Seed


# dog = Dog('Doggo', 10, 'Dobridj')
# print(dog.make_sound())
# meso = Meat(10)
# krastavica = Vegetable(10)
# print(meso.quantity)
#
# mishka = Mouse('Jerry', 10, 'hralupa')
# print(mishka.food_eaten, 'mishka food eaten', mishka.weight)
# print(mishka.feed(meso))
# mishka.feed(krastavica)
# print(mishka.food_eaten, 'mishka food eaten', mishka.weight, 'mishka weight')
# print(mishka)

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)