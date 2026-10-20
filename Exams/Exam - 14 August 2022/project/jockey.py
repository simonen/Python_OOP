from project.horse_specification.horse import Horse


class Jockey:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.horse: Horse | None = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.split():
            raise ValueError("Name should contain at least one character!")

        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 18:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")

        self._age = value