from project.car import Car
from project.vehicle import Vehicle


class SportsCar(Car):
    def __init__(self):
        Car.__init__(self)

    def race(self):
        return 'racing...'
