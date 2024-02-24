from project.mammal import Mammal
from project.reptile import Reptile
from project.lizard import Lizard
from project.snake import Snake
from project.gorilla import Gorilla
from project.bear import Bear

mammal = Mammal('Stella')

print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
reptile = Reptile("John")
print(reptile.__class__.__bases__[0].__name__)

lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)

bear = Bear("Grills")
print(bear.__class__.__bases__[0].__name__)
print(bear.name)

snake = Snake("Island")
print(snake.__class__.__bases__[0].__name__)
print(snake.name)

gorilla = Gorilla("Island")
print(gorilla.__class__.__bases__[0].__name__)
print(gorilla.name)
