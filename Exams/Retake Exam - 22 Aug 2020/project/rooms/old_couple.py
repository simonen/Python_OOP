from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove


class OldCouple(Room):
    _ROOM_COST = 15

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension * 2, members_count=2)
        self.appliances: list = [TV(), Fridge(), Stove()] * self.members_count
