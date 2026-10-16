from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.robots.base_robot import BaseRobot


class RobotsManagingApp:
    def __init__(self):
        self.robots: list[BaseRobot] = []
        self.services: list[BaseService] = []

    def add_service(self, service_type: str, name: str) -> str:
        service_types = {"MainService": MainService,
                         "SecondaryService": SecondaryService}
        if service_type not in service_types:
            raise Exception("Invalid service type!")

        service = service_types[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        robot_types = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
        if robot_type not in robot_types:
            raise Exception("Invalid robot type!")

        robot = robot_types[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def _find_robot(self, name: str, store: list) -> BaseRobot | None:
        robot = next((x for x in store if x.name == name), None)
        return robot

    def _find_service(self, name: str) -> BaseService | None:
        service = next((x for x in self.services if x.name == name), None)
        return service

    def _get_robot(self, name: str, store: list[BaseRobot]) -> BaseRobot:
        robot = self._find_robot(name, store)
        if robot is None:
            raise Exception("Robot not found")
        return robot

    def _get_service(self, name: str) -> BaseService:
        service = self._find_service(name)
        if service is None:
            raise Exception("Service not found")
        return service

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = self._get_robot(robot_name, self.robots)
        service = self._get_service(service_name)

        valid_pairs = {MaleRobot: MainService, FemaleRobot: SecondaryService}
        if valid_pairs[type(robot)] != type(service):
            return "Unsuitable service."

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = self._get_service(service_name)
        robot = self._get_robot(robot_name, service.robots)

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = self._get_service(service_name)

        if len(service.robots) == 0:
            raise Exception("No robots")

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str) -> str:
        service = self._get_service(service_name)
        total_robot_price = sum(x.price for x in service.robots)

        if service is None:
            raise Exception("Service does not exist!")

        return f"The value of service {service_name} is {total_robot_price:.2f}."

    def __str__(self) -> str:
        res = [service.details() for service in self.services]
        return "\n".join(res)