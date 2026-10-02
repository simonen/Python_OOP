from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        ...

    def __repr__(self) -> str:
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"


class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow meow!"

class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender='Male')

    def make_sound(self):
        return "Hiss"

class Kitten(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender='Female')

    def make_sound(self):
        return "Meow"

dog = Dog("Rocky", 3, "Male")
print(dog.make_sound())
print(dog)
tomcat = Tomcat("Tom", 6)
print(tomcat.make_sound())
print(tomcat)
kitten = Kitten("Kiki", 1)
print(kitten.make_sound())
print(kitten)
cat = Cat("Johnny", 7, "Male")
print(cat.make_sound())
print(cat)