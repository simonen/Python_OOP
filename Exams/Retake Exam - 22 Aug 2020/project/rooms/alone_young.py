from project.appliances.appliance import Appliance
from project.rooms.room import Room
from project.appliances.tv import TV


class AloneYoung(Room):
    _ROOM_COST = 10

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, members_count=1)
        self.appliances: list[Appliance] = [TV()]
