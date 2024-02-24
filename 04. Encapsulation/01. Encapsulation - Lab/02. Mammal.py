class Mammal:

    __kingdom = 'animals'

    def __init__(self, name: str, type: str, sound: str) -> None:
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self) -> str:
        return Mammal.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


mam = Mammal('Pen4o', 'cat', 'bark')

print(mam.get_kingdom())
