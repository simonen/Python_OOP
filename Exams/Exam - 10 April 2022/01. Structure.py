from project.controller import Controller
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food

controller = Controller()
apple = Food("apple", 110)
cheese = Food("cheese", 200)
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
third_player = Player('Xopxe', 15, 91)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
# print(controller.duel("Peter", "Lilly"))
print(controller.add_player(third_player))
print(controller.sustain("Lilly", "Drink"))
print('-----')
first_player.stamina = 30
controller.next_day()
print(controller)
print('-----')
print(controller.sustain("Peter", "Food"))
# print(controller.duel("Peter", "Lilly"))
# print(first_player)
# print(second_player)
first_player.age = 19
controller.next_day()
first_player.stamina = 30
print(controller)
print(controller.sustain('Peter', 'Voda'))

print(first_player.need_sustenance)