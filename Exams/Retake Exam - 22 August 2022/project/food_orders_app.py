from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    _VALID_MEALS = {"Dessert": Dessert, "MainDish": MainDish, "Starter": Starter}
    _RECEIPT = 0

    def __init__(self) -> None:
        self.menu: list[Meal] = []
        self.clients_list: list[Client] = []

    @property
    def menu_ready(self):
        return True if len(self.menu) >= 5 else False

    def _find_meal(self, meal_name: str) -> Meal | None:
        return next((meal for meal in self.menu if meal.name == meal_name), None)

    def _find_client(self, phone_number: str) -> Client | None:
        client = next((c for c in self.clients_list if c.phone_number == phone_number), None)
        return client

    def register_client(self, client_phone_number: str) -> str:
        client = self._find_client(client_phone_number)
        if client is not None:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal) -> None:
        new_meals = [meal for meal in meals if meal.__class__.__name__ in self._VALID_MEALS]
        self.menu += new_meals

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        meal_details = [meal.details() for meal in self.menu]
        return "\n".join(meal_details)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities) -> str:
        if not self.menu_ready:
            raise Exception("The menu is not ready!")

        client = self._find_client(client_phone_number)
        if client is None:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        to_add: list[tuple[Meal, int]] = []
        total = 0
        # Pass 1: Validate and collect
        for meal_name, quantity in meal_names_and_quantities.items():
            meal = self._find_meal(meal_name)
            if meal is None:
                raise Exception(f"{meal_name} is not on the menu!")

            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

            to_add.append((meal, quantity))
            total += meal.price * quantity
        # Pass 2 Commit: Mutate the menu items only after everything validated
        for meal, quantity in to_add:
            meal.quantity -= quantity
            client.shopping_cart.append(type(meal)(meal.name, meal.price, quantity))

        client.bill += total
        ordered_meals = ", ".join(x.name for x in client.shopping_cart)
        return f"Client {client_phone_number} successfully ordered {ordered_meals} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self._find_client(client_phone_number)
        if client is None:
            return None

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for item in client.shopping_cart:
            meal = self._find_meal(item.name)
            meal.quantity += item.quantity
            client.bill = 0
            client.shopping_cart = []

        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self._find_client(client_phone_number)
        if client is None:
            return None

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        paid_bill = client.bill
        client.bill = 0
        client.shopping_cart = []
        self._RECEIPT += 1

        return f"Receipt #{self._RECEIPT} with total amount of {paid_bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self) -> str:
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
