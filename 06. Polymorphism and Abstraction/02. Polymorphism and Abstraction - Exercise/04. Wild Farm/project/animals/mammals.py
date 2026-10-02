from project.animals.animal import Mammal
from project.food import Vegetable
from project.food import Fruit
from project.food import Meat


class Mouse(Mammal):
    FOOD = [Vegetable, Fruit]
    WEIGHT_INCREASE_BY = 0.10
    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    WEIGHT_INCREASE_BY = 0.40
    FOOD = [Meat]
    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    FOOD = [Vegetable, Meat]
    WEIGHT_INCREASE_BY = 0.30
    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    FOOD = [Meat]
    WEIGHT_INCREASE_BY = 1.00
    def make_sound(self):
        return "ROAR!!!"
