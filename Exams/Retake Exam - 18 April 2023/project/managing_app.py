from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.route import Route


class ManagingApp:
    def __init__(self):
        self.users: list[User] = []
        self.vehicles: list[BaseVehicle] = []
        self.routes: list[Route] = []

    def _find_by_driving_license(self, driving_license_number: str) -> User | None:
        user = next((x for x in self.users if x.driving_license_number == driving_license_number), None)
        return user

    def _find_route_by_id(self, route_id: int) -> Route | None:
        route = next((x for x in self.routes if x.route_id == route_id), None)
        return route

    def _find_vehicle_by_license_number(self, license_plate_number: str) -> BaseVehicle | None:
        vehicle = next((x for x in self.vehicles if x.license_plate_number == license_plate_number), None)
        return vehicle

    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
        if any(x for x in self.users if x.driving_license_number == driving_license_number):
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:
        valid_vehicles = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}
        if vehicle_type not in valid_vehicles:
            return f"Vehicle type {vehicle_type} is inaccessible."
        if any(x for x in self.vehicles if x.license_plate_number == license_plate_number):
            return f"{license_plate_number} belongs to another vehicle."

        vehicle = valid_vehicles[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float) -> str:
        route_id = len(self.routes) + 1
        if any(x for x in self.routes if x.start_point == start_point and x.end_point == end_point and x.length == length):
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        if any(x for x in self.routes if x.start_point == start_point and x.end_point == end_point and x.length < length):
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        longer_route = next((x for x in self.routes if x.start_point == start_point and x.end_point == end_point and x.length > length), None)
        if longer_route is not None:
            longer_route.is_locked = True

        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def _valid_route(self, route_id: int) -> Route:
        route = self._find_route_by_id(route_id)
        if route is not None:
            return route
        raise Exception(f"Route: {route_id} not found")

    def _valid_vehicle(self, license_plate_number: str) -> BaseVehicle:
        vehicle = self._find_vehicle_by_license_number(license_plate_number)
        if vehicle is not None:
            return vehicle
        raise Exception(f"Vehicle with license plate number: {license_plate_number} not found.")

    def _valid_user(self, driving_license_number: str) -> User:
        user = self._find_by_driving_license(driving_license_number)
        if user is not None:
            return user
        raise Exception(f"User with driving license: {driving_license_number} not found.")

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool) -> str:
        user = self._valid_user(driving_license_number)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = self._valid_vehicle(license_plate_number)
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = self._valid_route(route_id)
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int) -> str:
        sorted_damaged = sorted((x for x in self.vehicles if x.is_damaged), key=lambda x: (x.brand, x.model))
        if len(sorted_damaged) < count:
            count = len(sorted_damaged)

        for i in range(count):
            sorted_damaged[i].is_damaged = False
            sorted_damaged[i].recharge()

        return f"{count} vehicles were successfully repaired!"

    def users_report(self) -> str:
        res = ["*** E-Drive-Rent ***"]
        sorted_users = sorted(self.users, key=lambda x: x.rating, reverse=True)
        res.extend(map(str, sorted_users))

        return "\n".join(res)
