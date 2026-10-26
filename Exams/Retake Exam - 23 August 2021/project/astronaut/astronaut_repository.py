from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts: list[Astronaut] = []

    def add(self, astronaut: Astronaut) -> None:
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut) -> None:
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str) -> Astronaut | None:
        return next((astro for astro in self.astronauts if astro.name == name), None)