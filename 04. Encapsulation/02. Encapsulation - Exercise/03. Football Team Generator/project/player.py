class Player:

    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int) -> None:
        self.name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return '\n'.join([f"Player: {self.name}", f"Sprint: {self.__sprint}", f"Dribble: {self.__dribble}",
                          f"Passing: {self.__passing}", f"Shooting: {self.__shooting}"])
