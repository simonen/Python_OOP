from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00

    def drive(self, mileage: float):
        if mileage > self.max_mileage:  # Undefined by task
            mileage = self.max_mileage

        extra_consumption_factor = 5
        battery_used = round(mileage / self.max_mileage * 100) + extra_consumption_factor
        self.battery_level -= battery_used
