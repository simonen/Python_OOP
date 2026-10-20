from project.booths.booth import Booth


class OpenBooth(Booth):
    _PRICE = 2.50

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * OpenBooth._PRICE
        self.is_reserved = True
