from project.booths.booth import Booth


class PrivateBooth(Booth):
    _PRICE = 3.50

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * PrivateBooth._PRICE
        self.is_reserved = True
