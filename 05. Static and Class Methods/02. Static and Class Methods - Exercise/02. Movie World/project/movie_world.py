from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer) -> None:
        if MovieWorld.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if MovieWorld.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        dvd = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)
        customer = next((customer for customer in self.customers if customer.id == customer_id), None)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True

        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id) -> str:
        dvd = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)
        customer = next((customer for customer in self.customers if customer.id == customer_id), None)
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        return '\n'.join(map(str, self.customers)) + '\n' + '\n'.join(map(str, self.dvds))
