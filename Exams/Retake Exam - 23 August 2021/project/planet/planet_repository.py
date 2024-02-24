from typing import List
from project.planet.planet import Planet


class PlanetRepository:

    def __init__(self):
        self.planets: List[Planet] = []

    def add(self, planet: Planet) -> None:
        self.planets.append(planet)

    def remove(self, planet: Planet) -> None:
        self.planets.remove(planet)

    def find_by_name(self, name: str) -> str:
        planet = next((p for p in self.planets if p.name == name), None)
        return planet
