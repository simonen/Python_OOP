from project.appliances.appliance import Appliance
from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCouple(Room):
    _ROOM_COST = 20

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, members_count=2)
        self.appliances: list[Appliance] = [TV(), Fridge(), Laptop()] * 2
