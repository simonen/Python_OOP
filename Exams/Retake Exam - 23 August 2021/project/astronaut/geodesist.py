from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    @property
    def _INITIAL_OXYGEN(self) -> int:
        return 50
