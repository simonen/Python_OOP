from typing import List
from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def get_monthly_consumptions(self) -> str:
        total_consumption = sum([r.expenses + r.room_cost for r in self.rooms])
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self) -> str:
        res = []
        for room in self.rooms.copy():
            if room.budget >= room.expenses + room.room_cost:
                room.budget -= (room.expenses + room.room_cost)
                res.append(f"{room.family_name} paid {(room.expenses + room.room_cost):.2f}$ and have "
                           f"{room.budget:.2f}$ left.")
            else:
                res.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)

        return '\n'.join(res)

    def status(self) -> str:
        res = [f"Total population: {sum(x.members_count for x in self.rooms)}"]
        for room in self.rooms:
            res.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, "
                       f"Expenses: {room.expenses:.2f}$")

            if room.children:
                for i, child in enumerate(room.children):
                    res.append(f"--- Child {i + 1} monthly cost: {(child.cost * 30):.2f}$")

            app_cost = sum(x.get_monthly_expense() for x in room.appliances)
            res.append(f"--- Appliances monthly cost: {app_cost:.2f}$")

        return '\n'.join(res)
