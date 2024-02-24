class Player:

    all_players = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Name not valid!")

        if value in Player.all_players:
            raise Exception(f"Name {value} is already used!")

        Player.all_players.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.__stamina < 100

    def __str__(self) -> str:
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
