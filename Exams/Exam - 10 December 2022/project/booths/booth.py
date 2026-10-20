from abc import ABC, abstractmethod

from project.delicacies.delicacy import Delicacy


class Booth(ABC):
    def __init__(self, booth_number: int, capacity: int) -> None:
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders: list[Delicacy] = []
        self.price_for_reservation: float = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value: int):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self._capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        ...

    # def __repr__(self):
    #     orders = list(map(lambda x: x.price, self.delicacy_orders))
    #     bill = sum(orders)
    #     return f"boot number: {self.booth_number}, capacity: {self.capacity}," \
    #            f" orders: {list(map(lambda x: x.price, self.delicacy_orders))}, bill: {bill}, price_for_reservation: {self.price_for_reservation}, reserved: {self.is_reserved}"
