from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    _VALID_DECORATIONS = {"Ornament": Ornament, "Plant": Plant}
    _VALID_AQUARIUMS = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
    _VALID_FISH = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}

    def __init__(self) -> None:
        self.decorations_repository: DecorationRepository = DecorationRepository()
        self.aquariums: list[BaseAquarium] = []

    def _get_aquarium(self, aquarium_name: str) -> BaseAquarium:
        aquarium = next((x for x in self.aquariums if x.name == aquarium_name), None)
        if aquarium is not None:
            return aquarium

        raise Exception(f"No aquarium {aquarium_name} in {self.aquariums}!*")

    def add_aquarium(self, aquarium_type: str, aquarium_name: str) -> str:
        if aquarium_type not in self._VALID_AQUARIUMS:
            return "Invalid aquarium type."

        aquarium = self._VALID_AQUARIUMS[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str) -> str:
        if decoration_type not in Controller._VALID_DECORATIONS:
            return "Invalid decoration type."

        decoration = Controller._VALID_DECORATIONS[decoration_type]()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str) -> str:
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self._get_aquarium(aquarium_name)
        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float) -> str:
        if fish_type not in self._VALID_FISH:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self._get_aquarium(aquarium_name)
        if len(aquarium.fish) == aquarium.capacity:
            return "Not enough capacity."

        if fish_type not in aquarium.FISH_TYPES:
            return "Water not suitable."

        fish = self._VALID_FISH[fish_type](fish_name, fish_species, price)
        aquarium.add_fish(fish)
        return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str) -> str:
        aquarium = self._get_aquarium(aquarium_name)
        for fish in aquarium.fish:
            fish.eat()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str) -> str:
        aquarium = self._get_aquarium(aquarium_name)
        decoration_value = sum(x.price for x in aquarium.decorations)
        fish_value = sum(x.price for x in aquarium.fish)
        return f"The value of Aquarium {aquarium_name} is {(decoration_value + fish_value):.2f}."

    def report(self) -> str:
        res = [str(aq) for aq in self.aquariums]
        return "\n".join(res)
