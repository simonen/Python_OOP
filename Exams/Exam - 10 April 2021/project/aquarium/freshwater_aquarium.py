from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    CAPACITY = 50
    FISH_TYPES = ["FreshwaterFish"]

    def __init__(self, name: str) -> None:
        super().__init__(name, type(self).CAPACITY)
