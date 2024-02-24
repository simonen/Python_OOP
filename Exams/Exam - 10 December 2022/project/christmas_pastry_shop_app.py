from typing import List
from project.booths.booth import Booth
from project.delicacies.delicacy import Delicacy


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str or None:
        if any(d for d in self.delicacies if d.name == name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ["Gingerbread", "Stolen"]:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = globals()[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str or None:
        if any(b for b in self.booths if b.booth_number == booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = globals()[''.join(type_booth.split())](booth_number, capacity)
        self.booths.append(new_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) -> str or None:
        booth = next((b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people), None)
        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str or None:
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next(b for b in self.booths if b.booth_number == booth_number)
        bill = booth.price_for_reservation + sum(list(map(lambda x: x.price, booth.delicacy_orders)))
        self.income += bill

        booth.price_for_reservation = 0
        booth.is_reserved = False
        booth.delicacy_orders = []

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self) -> str:
        return f"Income: {self.income:.2f}lv."
