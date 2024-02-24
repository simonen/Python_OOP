from project.animal import Animal
from project.mammal import Mammal


class Gorilla(Mammal):

    def __init__(self, name: str):
        self.name = name