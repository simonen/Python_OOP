from typing import List
from abc import abstractmethod, ABC
from project.delicacies.delicacy import Delicacy


class Booth(ABC):

    def __init__(self, booth_number: int,  capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders: List[Delicacy] = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")

        self.__capacity = value

    # def __repr__(self):
    #     orders = list(map(lambda x: x.price, self.delicacy_orders))
    #     bill = sum(orders)
    #     return f"boot number: {self.booth_number}, capacity: {self.capacity}," \
    #            f" orders: {list(map(lambda x: x.price, self.delicacy_orders))}, bill: {bill}, price_for_reservation: {self.price_for_reservation}, reserved: {self.is_reserved}"
