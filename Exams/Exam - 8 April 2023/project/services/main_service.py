from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        robots = [x.name for x in self.robots]
        return f"{self.name} Main Service:\nRobots: {' '.join(robots) if robots else 'none'}"
