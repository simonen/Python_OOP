from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeak"


class Flyable:
    def fly(self):
        return f"{self.__class__.__name__} is "


class Walkable:

    def walk(self):
        return f"{self.__class__.__name__}"


class RobotDuck(Duck, Flyable, Walkable):
    HEIGHT = 3

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    def walk(self):
        return f"{super().walk()} 'is walking'"

    def fly(self):
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


rubber = RubberDuck
print(rubber.quack())
robot = RobotDuck()
print(robot.walk())
print(robot.quack())
robot.fly()
robot.fly()
robot.fly()
print(robot.height)
robot.fly()
print(robot.height)
print(Walkable().walk())