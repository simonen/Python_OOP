from abc import ABC


class Car(ABC):
    SPEED_LIMIT: range

    def __init__(self, model: str, speed_limit: int) -> None:
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value: str):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")

        self._model = value

    @property
    def speed_limit(self):
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, value: int):
        if value not in self.SPEED_LIMIT:
            raise ValueError(f"Invalid speed limit! Must be between "
                             f"{min(self.SPEED_LIMIT)} and {max(self.SPEED_LIMIT)}!")

        self._speed_limit = value

    def __repr__(self):
        return f"{self.model}, {self.speed_limit}"
