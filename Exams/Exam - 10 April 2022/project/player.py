class Player:
    __PLAYER_NAMES = []

    def __init__(self, name: str, age: int, stamina: int = 100) -> None:
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.split():
            raise ValueError("Name not valid!")

        if value in Player.__PLAYER_NAMES:
            raise Exception(f"Name {value} is already used!")

        Player.__PLAYER_NAMES.append(value)

        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self._age = value

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value: int):
        if not 0 <= value <= 100:
            raise ValueError("Stamina not valid!")

        self._stamina = value

    def __str__(self) -> str:
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
