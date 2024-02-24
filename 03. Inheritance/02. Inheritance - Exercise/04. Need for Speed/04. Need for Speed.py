from project.vehicle import Vehicle
from project.car import Car
from project.family_car import FamilyCar
from project.sport_car import SportCar
from project.motorcycle import Motorcycle
from project.race_motorcycle import RaceMotorcycle
from project.cross_motorcycle import CrossMotorcycle


vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
race_motorcycle = RaceMotorcycle(100, 120)
print(race_motorcycle.__class__.__bases__[0].__name__)

race_motorcycle.drive(10)
print(race_motorcycle.fuel)
car = Car(200, 300)
print(car.__class__.__bases__[0].__name__)
lambo = SportCar(300, 200)
lambo.drive(30)
print(lambo.fuel)
print(lambo.__class__.__bases__[0].__name__)
print(lambo.fuel_consumption)
car.drive(10)
print(car.DEFAULT_FUEL_CONSUMPTION)
motor = Motorcycle(30, 600)
print(motor.fuel, motor.fuel_consumption)
motor.drive(100)
print(motor.fuel)
print(motor.fuel_consumption)
cross = CrossMotorcycle(300, 400)
cross.drive(20)
print(cross.fuel)
race = RaceMotorcycle(300, 400)
race.drive(20)
print(race.fuel)