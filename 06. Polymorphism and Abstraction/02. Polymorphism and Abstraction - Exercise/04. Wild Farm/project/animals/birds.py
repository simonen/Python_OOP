from project.animals.animal import Bird
from project.food import *


class Hen(Bird):
    FOOD = [Vegetable, Meat, Seed, Fruit]
    WEIGHT_INCREASE_BY = 0.35

    def make_sound(self):
        return "Cluck"


class Owl(Bird):
    FOOD = [Meat]
    WEIGHT_INCREASE_BY = 0.25

    def make_sound(self):
        return "Hoot Hoot"
