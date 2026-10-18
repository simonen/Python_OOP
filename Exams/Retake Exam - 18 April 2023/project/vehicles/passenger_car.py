from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def drive(self, mileage: float) -> None:
        if mileage > self.max_mileage:  # Undefined by task
            mileage = self.max_mileage

        battery_used = round(mileage / self.max_mileage * 100)
        self.battery_level -= battery_used
