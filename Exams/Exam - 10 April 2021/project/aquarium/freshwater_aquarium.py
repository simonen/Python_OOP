from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    _CAPACITY = 50
    def __init__(self, name: str) -> None:
        super().__init__(name, type(self)._CAPACITY)
