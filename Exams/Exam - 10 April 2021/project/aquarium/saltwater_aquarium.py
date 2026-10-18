from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    CAPACITY = 25
    FISH_TYPES = ["SaltwaterFish"]

    def __init__(self, name: str) -> None:
        super().__init__(name, type(self).CAPACITY)
