from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    _DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    _BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self) -> None:
        self.booths: list[Booth] = []
        self.delicacies: list[Delicacy] = []
        self.income: float = 0

    def _find_by_booth_number(self, booth_number: int) -> Booth | None:
        booth = next((x for x in self.booths if x.booth_number == booth_number), None)
        return booth

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in ChristmasPastryShopApp._DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if any(x for x in self.delicacies if x.name == name):
            raise Exception(f"{name} already exists!")

        delicacy = ChristmasPastryShopApp._DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in ChristmasPastryShopApp._BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")
        if self._find_by_booth_number(booth_number) is not None:
            raise Exception(f"Booth number {booth_number} already exists!")

        booth = ChristmasPastryShopApp._BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = next((x for x in self.booths if not x.is_reserved and x.capacity >= number_of_people), None)
        if booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self._find_by_booth_number(booth_number)
        delicacy = next((x for x in self.delicacies if x.name == delicacy_name), None)
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self._find_by_booth_number(booth_number)
        bill = booth.price_for_reservation + sum(x.price for x in booth.delicacy_orders)
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False

        self.income += bill

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."