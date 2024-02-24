from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet_repository import PlanetRepository
from project.planet.planet import Planet
from project.astronaut.astronaut_repository import AstronautRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.complete = 0
        self.incomplete = 0

    def add_astronaut(self, astronaut_type: str, name: str) -> str:
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        new_astro = globals()[astronaut_type](name)
        self.astronaut_repository.add(new_astro)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str) -> str or None:
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items.extend(items.split(", "))
        self.planet_repository.add(new_planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str) -> str or None:
        astro = self.astronaut_repository.find_by_name(name)
        if not astro:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astro)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self) -> None:
        for astro in self.astronaut_repository.astronauts:
            astro.oxygen += 10

    def send_on_mission(self, planet_name: str) -> str or None:
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        oxygen_raking = sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)
        crew = list(filter(lambda x: x.oxygen > 30, oxygen_raking))[:5]

        if not crew:
            raise Exception("You need at least one astronaut to explore the planet!")

        collectors = 0
        while crew and planet.items:
            if not crew[0].backpack:
                collectors += 1
            if crew[0].oxygen > 0:
                crew[0].backpack.append(planet.items.pop())
                crew[0].breathe()
            if crew[0].oxygen == 0:
                crew.pop(0)

        if not planet.items:
            self.complete += 1
            return f"Planet: {planet_name} was explored. {collectors} astronauts participated in collecting items."

        self.incomplete += 1
        return "Mission is not completed."

    def report(self) -> str:
        res = [f"{self.complete} successful missions!",
               f"{self.incomplete} missions were not completed!", "Astronauts' info:"]

        for astro in self.astronaut_repository.astronauts:
            res.extend(astro.details())

        return '\n'.join(res)
