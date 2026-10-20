from project.jockey import Jockey


class HorseRace:
    _VALID_RACE = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self, race_type: str) -> None:
        self.race_type = race_type
        self.jockeys: list[Jockey] = []

    @property
    def race_type(self):
        return self._race_type

    @race_type.setter
    def race_type(self, value: str):
        if value not in self._VALID_RACE:
            raise ValueError("Race type does not exist!")

        self._race_type = value