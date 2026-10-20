class Driver:
    def __init__(self, name: str) -> None:
        self.name = name
        self.car = None
        self.number_of_wins: int = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.split():
            raise ValueError("Name should contain at least one character!")

        self._name = value
