from abc import abstractmethod, ABC


class Horse(ABC):

    def __init__(self, name: str, speed: int):
        self.name = name
        self._speed = None
        self.speed = speed  # We use the setter method here to validate the speed
        self.is_taken: bool = False

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        max_speed = self._get_max_speed()
        if new_speed > max_speed:
            raise ValueError("Horse speed is too high!")
        self._speed = new_speed

    def _get_max_speed(self):
        pass  # This is meant to be overridden in subclasses

    @abstractmethod
    def train(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")

        self.__name = value