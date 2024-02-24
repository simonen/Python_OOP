from typing import List
from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.table import Table
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float) -> str or None:
        if any(f for f in self.food_menu if f.name == name):
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in ["Bread", "Cake"]:
            new_food = globals()[food_type](name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str) -> str or None:
        if any(d for d in self.drinks_menu if d.name == name):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in ["Tea", "Water"]:
            new_drink = globals()[drink_type](name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int) -> str or None:
        if any(t for t in self.tables_repository if t.table_number == table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in ["InsideTable", "OutsideTable"]:
            new_table = globals()[table_type](table_number, capacity)
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int) -> str:
        table = next((t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people), None)
        if not table:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_item(self, table_number, *items, item_type: str):
        menu = {
            'food': [self.food_menu, lambda: table.order_food(product) if product else not_present.append(item)],
            'drink': [self.drinks_menu, lambda: table.order_drink(product) if product else not_present.append(item)]
        }

        table = next((t for t in self.tables_repository if t.table_number == table_number), None)
        if not table:
            return f"Could not find table {table_number}"

        not_present = []
        for item in items:
            product = next((p for p in menu[item_type][0] if p.name == item), None)
            menu[item_type][1]()

        ordered_foods = '\n'.join(map(str, table.food_orders if item_type == 'food' else table.drink_orders))
        not_ordered = '\n'.join(not_present)
        return f"Table {table_number} ordered:\n{ordered_foods}\n{self.name} does not have in the menu:\n{not_ordered}"

    def order_food(self, table_number: int, *foods):
        return self.order_item(table_number, *foods, item_type='food')

    def order_drink(self, table_number: int, *drinks):
        return self.order_item(table_number, *drinks, item_type='drink')

    def leave_table(self, table_number: int):
        table = next((t for t in self.tables_repository if t.table_number == table_number), None)
        if table:
            table_bill = table.get_bill()
            self.total_income += table_bill
            table.clear()
            return f"Table: {table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        free_tables = list(filter(lambda x: not x.is_reserved, self.tables_repository))
        info = []
        for table in free_tables:
            info.append(table.free_table_info())

        return '\n'.join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
