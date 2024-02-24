from abc import abstractmethod, ABC


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def drive(self, distance) -> None:
        if self.fuel_quantity >= (self.fuel_consumption + 0.9) * distance:
            self.fuel_quantity -= (self.fuel_consumption + 0.9) * distance

    def refuel(self, fuel) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def drive(self, distance) -> None:
        if self.fuel_quantity >= (self.fuel_consumption + 1.6) * distance:
            self.fuel_quantity -= (self.fuel_consumption + 1.6) * distance

    def refuel(self, fuel) -> None:
        self.fuel_quantity += 0.95 * fuel


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