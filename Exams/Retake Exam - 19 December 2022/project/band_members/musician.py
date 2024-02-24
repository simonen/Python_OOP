from abc import abstractmethod, ABC
from typing import List


class Musician(ABC):
    VALID_SKILLS = {"Guitarist": ["play metal", "play rock", "play jazz"],
                    "Drummer": ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"],
                    "Singer": ["sing high pitch notes", "sing low pitch notes"]}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills: List[str] = []

    @abstractmethod
    def learn_new_skill(self, new_skill: str):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Musician name cannot be empty!")

        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")

        self.__age = value
