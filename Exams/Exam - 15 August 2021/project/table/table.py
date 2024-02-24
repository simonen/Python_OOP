from abc import ABC, abstractmethod
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from typing import List


class Table(ABC):

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: List[BakedFood] = []
        self.drink_orders: List[Drink] = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False

    def __repr__(self):
        return f"TN: {self.table_number}, C: {self.capacity}, FO: {self.food_orders}, " \
               f"DO: {self.drink_orders}, P: {self.number_of_people}, R: {self.is_reserved}"

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

        self.__capacity = value

    def reserve(self, number_of_people: int) -> None:
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood) -> None:
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink) -> None:
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum([x.price for x in self.food_orders]) + sum([x.price for x in self.drink_orders])

    def clear(self) -> None:
        self.is_reserved = False
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0

    def free_table_info(self):
        if not self.is_reserved and self.number_of_people == 0:
            return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"
