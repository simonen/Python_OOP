from project.product import Product
from project.product_repository import ProductRepository
from project.food import Food
from project.drink import Drink

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
print(repo)
repo.find("apple").decrease(5)
repo.find("apple").decrease(5)
repo.find("apple").decrease(5)
print(repo)
print()
print(repo)