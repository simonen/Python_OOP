from project.appliances.appliance import Appliance
from project.rooms.room import Room


class AloneOld(Room):
    _ROOM_COST = 10

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, members_count=1)
        self.appliances: list[Appliance] = []

