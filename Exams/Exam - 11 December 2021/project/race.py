from project.driver import Driver


class Race:
    def __init__(self, name: str) -> None:
        self.name = name
        self.drivers: list[Driver] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.split():
            raise ValueError("Name cannot be an empty string!")

        self._name = value