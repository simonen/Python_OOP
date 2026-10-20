from abc import ABC,abstractmethod


class Horse(ABC):
    _SPEED_INCREASE: int
    _MAX_SPEED: int

    def __init__(self, name: str, speed: int) -> None:
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")

        self._name = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value: int):
        if value > self._MAX_SPEED:
            raise ValueError("Horse speed is too high!")

        self._speed = value

    def train(self):
        self.speed += self._SPEED_INCREASE
