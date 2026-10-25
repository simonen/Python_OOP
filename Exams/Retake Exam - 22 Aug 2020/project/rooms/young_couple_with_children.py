from project.appliances.appliance import Appliance
from project.people.child import Child
from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):
    _ROOM_COST = 30

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_two + salary_one, members_count=2)
        self.children: list[Child] = [*children]
        self.appliances: list[Appliance] = [TV(), Fridge(), Laptop()] * (self.members_count + len(self.children))
