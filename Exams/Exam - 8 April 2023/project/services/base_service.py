from abc import abstractmethod, ABC
from typing import List
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot


class BaseService(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots: List[FemaleRobot, MaleRobot] = []

    @abstractmethod
    def details(self):
        pass

    @property
    def capacity(self) -> None:
        return self.__capacity

    @capacity.setter
    def capacity(self, value) -> None:
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")

        self.__capacity = value

    @property
    def name(self) -> None:
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Service name cannot be empty!")

        self.__name = value

    def increase_cap(self):
        self.__capacity += 1

    def decrease_cap(self):
        self.__capacity -= 1
        if self.__capacity < 0:
            self.__capacity = 0
