from project.dvd import DVD
from project.customer import Customer
from typing import TypeVar


T = TypeVar("T", DVD, Customer)


class MovieWorld:
    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def _find_by_id(self, item_id: int, store: list[T]) -> T | None:
        return next((x for x in store if x.id == item_id), None)

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self._find_by_id(customer_id, self.customers)
        dvd = self._find_by_id(dvd_id, self.dvds)

        if customer is None or dvd is None:      # Early returns to get rid of hinting
            return None

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd and dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"


    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = self._find_by_id(customer_id, self.customers)
        dvd = self._find_by_id(dvd_id, self.dvds)

        if customer is None or dvd is None:  # Early returns to get rid of hinting
            return None

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self) -> str:
        customers = [str(c) for c in self.customers]
        dvds = [str(d) for d in self.dvds]

        return "\n".join(customers + dvds)
