from abc import ABC,abstractmethod
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.robots.base_robot import BaseRobot


class BaseService(ABC):
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity
        self.robots: list[BaseRobot] = []

    @abstractmethod
    def details(self):
        ...

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.split():
            raise ValueError("Service name cannot be empty!")
        self._name = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value: int):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self._capacity = value
