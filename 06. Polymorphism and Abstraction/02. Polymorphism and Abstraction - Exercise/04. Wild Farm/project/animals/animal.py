from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):
    WEIGHT_INCREASE_BY: float
    FOOD = []

    def __init__(self, name: str, weight: float, food_eaten = 0) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        ...

    def feed(self, food: Food):
        if type(food) not in self.FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += (self.WEIGHT_INCREASE_BY * food.quantity)
        return None


class Mammal(Animal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten=0) -> None:
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Bird(Animal):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten = 0, ) -> None:
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
