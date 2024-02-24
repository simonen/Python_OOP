from typing import List
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot


class RobotsManagingApp:

    def __init__(self):
        self.robots: List[MaleRobot, FemaleRobot] = []
        self.services: List[MainService, SecondaryService] = []

    def add_service(self, service_type: str, name: str) -> str:
        if service_type not in ['MainService', 'SecondaryService']:
            raise Exception("Invalid service type!")

        new_service = globals()[service_type](name)
        self.services.append(new_service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str or None:

        if robot_type not in ["MaleRobot", "FemaleRobot"]:
            raise Exception("Invalid robot type!")

        new_robot = globals()[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str or None:
        robot = next(b for b in self.robots if b.name == robot_name)
        service = next(s for s in self.services if s.name == service_name)
        valid = {MaleRobot: MainService, FemaleRobot: SecondaryService}
        if valid[robot.__class__] != service.__class__:
            return "Unsuitable service."

        if service.capacity == 0:
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        service.decrease_cap()

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = next(s for s in self.services if s.name == service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if not robot:
            raise Exception("No such robot in this service!")

        self.robots.append(robot)
        service.robots.remove(robot)
        service.increase_cap()

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = next(s for s in self.services if s.name == service_name)
        robots = [r for r in service.robots]
        [bot.eating() for bot in robots]

        return f"Robots fed: {len(robots)}."

    def service_price(self, service_name: str) -> str:

        service = next(s for s in self.services if s.name == service_name)
        price = sum(robot.price for robot in service.robots)

        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self) -> str:
        res = [service.details() for service in self.services]

        return '\n'.join(res)
