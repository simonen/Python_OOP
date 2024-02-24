from project.decoration.base_decoration import BaseDecoration
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament
from project.decoration.decoration_repository import DecorationRepository
from project.fish.base_fish import BaseFish
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from typing import List


class Controller:

    def __init__(self):
        self.decorations_repository: DecorationRepository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str) -> str:
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."

        new_aqua = globals()[aquarium_type](aquarium_name)
        self.aquariums.append(new_aqua)

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str) -> str:
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."

        decoration = globals()[decoration_type]()
        self.decorations_repository.add(decoration)

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str) -> str:
        aqua = next((a for a in self.aquariums if a.name == aquarium_name), None)
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if isinstance(decoration, str) or not aqua:
            return f"There isn't a decoration of type {decoration_type}."

        aqua.decorations.append(decoration)
        self.decorations_repository.remove(decoration)

        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float) -> str or None:
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."

        aqua = next((a for a in self.aquariums if a.name == aquarium_name), None)
        if not aqua:
            return None

        if (fish_type == 'FreshwaterFish' and aqua.__class__.__name__ == 'SaltwaterAquarium') or \
            (fish_type == "SaltwaterFish" and aqua.__class__.__name__ == "FreshwaterAquarium"):
            return "Water not suitable."

        fish = globals()[fish_type](fish_name, fish_species, price)
        return aqua.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aqua = next((a for a in self.aquariums if a.name == aquarium_name), None)
        if aqua:
            aqua.feed()
            return f"Fish fed: {len(aqua.fish)}"

    def calculate_value(self, aquarium_name: str):
        aqua = next((a for a in self.aquariums if a.name == aquarium_name), None)
        if aqua:
            fish_value = sum(f.price for f in aqua.fish)
            decor_value = sum(d.price for d in aqua.decorations)
            return f"The value of Aquarium {aquarium_name} is {(fish_value + decor_value):.2f}."

    def report(self):
        return '\n'.join([str(aqua) for aqua in self.aquariums])