from project.animal import Animal
from project.mammal import Mammal


class Bear(Mammal):

    def __init__(self, name: str):
        self.name = name