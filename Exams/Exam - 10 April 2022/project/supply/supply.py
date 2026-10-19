from abc import ABC, abstractmethod


class Supply(ABC):
    def __init__(self, name: str, energy: int) -> None:
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.split():
            raise ValueError("Name cannot be an empty string.")

        self._name = value

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value: int):
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")

        self._energy = value

    @abstractmethod
    def details(self):
        ...