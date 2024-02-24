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

from project.controller import Controller

controller = Controller()

print("---DECORATION REPO ADD---")
orna1 = Ornament()
plant1 = Plant()
print(controller.decorations_repository.add(orna1))
print(controller.decorations_repository.add(plant1))
print("---DECORATION REPO REMOVE---")
print(controller.decorations_repository.remove(plant1))
print(controller.decorations_repository.decorations)
print("---DECORATION REPO FIND---")
print(controller.decorations_repository.find_by_type('Ornament'))
print(controller.decorations_repository.find_by_type('Plant'))
print("---AQUARIUM ADD---")
print(controller.add_aquarium("FreshwaterAquarium", 'FreshAqua1'))
print(controller.add_aquarium("SaltwaterAquarium", 'SaltyAqua1'))
print('\n'.join(list(map(str, controller.aquariums))))
print()
print("---DECORATION ADD---")
print(list(map(lambda x: x.__class__.__name__, controller.decorations_repository.decorations)))
print(controller.add_decoration('Plant'))
print(controller.add_decoration('Ornament'))
print(controller.add_decoration('Ornament'))
print(controller.add_decoration('Plant'))
print(controller.add_decoration('Ornament'))
print("---DECORATION INSERT---")
# print(controller.decorations_repository.find_by_type('Plant'))
print(list(map(lambda x: x.__class__.__name__, controller.decorations_repository.decorations)))
print(controller.insert_decoration('FreshAqua1', 'Plant'))
print(controller.insert_decoration('FreshAqua1', 'Plant'))
print(controller.insert_decoration('FreshAqua1', 'Plant'))
print(controller.insert_decoration('FreshAqua1', 'Ornament'))
print(controller.insert_decoration('FreshAqua1', 'Ornament'))
print(list(map(lambda x: x.__class__.__name__, controller.decorations_repository.decorations)))
print(controller.aquariums[0].decorations)
print("---CONTROLLER: ADD FISH---")
print(controller.add_fish('FreshAqua1', 'FreshwaterFish', 'Fishko', 'Akula', 15))
print(controller.report())