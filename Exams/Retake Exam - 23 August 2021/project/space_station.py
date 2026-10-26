from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    DEBUG = True
    _COLOR = True
    _RESET, _DIM = "\033[0m", "\033[2m"
    _GREEN, _YELLOW, _RED, _CYAN = "\033[32m", "\033[33m", "\033[31m", "\033[36m"
    _ASTRONAUT_TYPES = {"Meteorologist": Meteorologist, "Geodesist": Geodesist, "Biologist": Biologist}

    def __init__(self):
        self.planet_repository: PlanetRepository = PlanetRepository()
        self.astronaut_repository: AstronautRepository = AstronautRepository()
        self.missions_ok = 0
        self.missions_fail = 0

    def _debug(self, msg, color=_CYAN):
        if not self.DEBUG:
            return
        c = color if self._COLOR else ""
        reset = self._RESET if self._COLOR else ""
        print(f"{c}[DEBUG]: {msg}{reset}")

    def add_astronaut(self, astronaut_type: str, name: str) -> str:
        if astronaut_type not in self._ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        self.astronaut_repository.add(self._ASTRONAUT_TYPES[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str) -> str:
        if self.planet_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."


    def retire_astronaut(self, name: str) -> str:
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self) -> None:
        for astro in self.astronaut_repository.astronauts:
            astro.increase_oxygen(10)

    def send_on_mission(self, planet_name: str) -> str:
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        eligible = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        team = sorted(eligible, key=lambda x: -x.oxygen)[:5]

        if not team:
            raise Exception("You need at least one astronaut to explore the planet!")

        for participants, astro in enumerate(team, start=1) :
            self._debug(f"Astronaut id {participants} {astro.name} went to planet {planet_name}")
            self._debug(f"Items to collect: {len(planet.items)}", self._GREEN)
            while planet.items and astro.oxygen > 0:
                item = planet.items.pop()
                astro.backpack.append(item)
                astro.breathe()
                self._debug(f"Astronaut {astro.name} collected {item}")
            if not planet.items:
                self.missions_ok += 1
                return f"Planet: {planet_name} was explored. {participants} astronauts participated in collecting items."

        self.missions_fail += 1
        return  "Mission is not completed."

    def report(self) -> str:
        astro = [f"{str(a)}" for a in self.astronaut_repository.astronauts]
        res = [f"{self.missions_ok} successful missions!",
               f"{self.missions_fail} missions were not completed!",
               "Astronauts' info:"]

        return "\n".join(res + astro)