from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: list[Room] = []

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def get_monthly_consumptions(self) -> str:
        """Sum of room cost + appliance and children cost for a month"""
        total = sum(room.current_expenses for room in self.rooms)
        return f"Monthly consumption: {total :.2f}$."

    def pay(self) -> str:
        res = []
        rooms_paid = []
        for room in self.rooms:
            bill = room.current_expenses
            if room.budget >= bill:
                room.budget -= bill
                room.expenses = bill
                rooms_paid.append(room)
                res.append(f"{room.name} paid {room.expenses:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                res.append(f"{room.name} does not have enough budget and must leave the hotel.")

        self.rooms = rooms_paid

        return "\n".join(res)

    def status(self) -> str:
        hotel_residents = sum(x.count_residents() for x in self.rooms)
        res = [f"Total population: {hotel_residents}"]

        for room in self.rooms:
            res.append(f"{room.name} with {room.count_residents()} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            res += [f"--- Child {i + 1} monthly cost: {child.get_monthly_expense():.2f}$" for i, child in enumerate(room.children)]
            appliances_cost = sum(appliance.get_monthly_expense() for appliance in room.appliances)
            res.append(f"--- Appliances monthly cost: {appliances_cost:.2f}$")

        return "\n".join(res)
