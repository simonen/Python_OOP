from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    _DECREASE_AMOUNT = 15

    @property
    def _INITIAL_OXYGEN(self) -> int:
        return 90