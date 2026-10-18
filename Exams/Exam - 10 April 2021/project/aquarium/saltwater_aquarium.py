from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    _CAPACITY = 25

    def __init__(self, name: str) -> None:
        super().__init__(name, type(self)._CAPACITY)
