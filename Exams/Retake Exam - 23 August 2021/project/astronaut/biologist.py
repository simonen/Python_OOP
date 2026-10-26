from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    _DECREASE_AMOUNT = 5

    @property
    def _INITIAL_OXYGEN(self) -> int:
        return 70
