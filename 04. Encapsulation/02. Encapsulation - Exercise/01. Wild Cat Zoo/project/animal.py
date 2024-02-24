class Animal:

    MONEY_FOR_CARE = None

    def __init__(self, name: str, gender: str, age: int) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = self.MONEY_FOR_CARE

    def __repr__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
