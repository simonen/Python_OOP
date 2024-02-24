from typing import List
from project.meals.meal import Meal
from project.client import Client
import copy


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str) -> str or None:
        if any(c for c in self.clients_list if c.phone_number == client_phone_number):
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal) -> None:
        for meal in meals:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self) -> str or None:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return '\n'.join([m.details() for m in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities) -> str or None:
        client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        meals: List[Meal] = []
        total = 0
        temp_menu = copy.copy(self.menu)
        for meal_key, quantity in meal_names_and_quantities.items():
            meal = next((m for m in temp_menu if m.name == meal_key), None)
            if not meal:
                raise Exception(f"{meal_key} is not on the menu!")
            if quantity > meal.quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_key}!")

            user_meal = copy.copy(meal)
            user_meal.quantity = quantity
            meals.append(user_meal)
            total += (quantity * meal.price)
            meal.quantity -= quantity

        self.menu = temp_menu
        client.shopping_cart.extend(meals)
        client.bill += total

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(list(map(lambda x: x.name, client.shopping_cart)))} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str) -> str or None:
        client = next(c for c in self.clients_list if c.phone_number == client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            for item in self.menu:
                if meal.name == item.name:
                    item.quantity += meal.quantity

        self.empty_cart(client)

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str) -> str or None:
        client = next(c for c in self.clients_list if c.phone_number == client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        paid = client.bill
        self.empty_cart(client)
        self.receipt_id += 1

        return f"Receipt #{self.receipt_id} with total amount of " \
               f"{paid:.2f} was successfully paid for {client_phone_number}."

    def __str__(self) -> str:
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    @staticmethod
    def empty_cart(client: Client) -> None:
        client.shopping_cart = []
        client.bill = 0
