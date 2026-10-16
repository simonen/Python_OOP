from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15
    def __init__(self, name: str) -> None:
        super().__init__(name, self.CAPACITY)

    def details(self):
        robots = [x.name for x in self.robots]
        return f"{self.name} Secondary Service:\nRobots: {' '.join(robots) if robots else 'none'}"
