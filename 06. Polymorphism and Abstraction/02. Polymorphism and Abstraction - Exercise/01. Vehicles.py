from abc import abstractmethod, ABC


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    @abstractmethod
    def drive(self, distance) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel) -> None:
        pass

class Car(Vehicle):
    CONSUMPTION_INCREASE = 0.9

    def drive(self, distance) -> None:
        req_fuel = (self.fuel_consumption + self.CONSUMPTION_INCREASE) * distance
        if req_fuel <= self.fuel_quantity:
            self.fuel_quantity -= req_fuel

    def refuel(self, fuel: float | int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    FUEL_RETENTION = 0.95
    CONSUMPTION_INCREASE = 1.6

    def drive(self, distance) -> None:
        req_fuel = (self.fuel_consumption + self.CONSUMPTION_INCREASE) * distance
        if req_fuel <= self.fuel_quantity:
            self.fuel_quantity -= req_fuel

    def refuel(self, fuel: float | int) -> None:
        self.fuel_quantity += (fuel * self.FUEL_RETENTION)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
print()
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)