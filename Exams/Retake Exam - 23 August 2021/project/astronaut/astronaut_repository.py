from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from typing import List


class AstronautRepository:

    def __init__(self):
        self.astronauts: List[Astronaut] = []

    def add(self, astronaut: Astronaut) -> None:
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut) -> None:
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        astro = next((a for a in self.astronauts if a.name == name), None)
        return astro
