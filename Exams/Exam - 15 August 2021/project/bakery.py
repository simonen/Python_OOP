from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    _VALID_FOODS = {"Bread": Bread, "Cake": Cake}
    _VALID_DRINKS = {"Tea": Tea, "Water": Water}
    _VALID_TABLES = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}
    _ORDER_ATTRS = {"Food": ("food_menu", "food_orders"),
                   "Drink": ("drinks_menu", "drink_orders")}

    def __init__(self, name: str) -> None:
        self.name = name
        self.food_menu: list[BakedFood] = []
        self.drinks_menu: list[Drink] = []
        self.tables_repository: list[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.split():
            raise ValueError("Name cannot be empty string or white space!")

        self._name = value

    def _find_table(self, table_number: int):
        return next((x for x in self.tables_repository if x.table_number == table_number), None)

    def add_food(self, food_type: str, name: str, price: float):
        if food_type not in self._VALID_FOODS:
            return None

        if next((x for x in self.food_menu if x.name == name), None) is not None:
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = self._VALID_FOODS[food_type](name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        if drink_type not in self._VALID_DRINKS:
            return None

        if next((x for x in self.drinks_menu if x.name == name), None) is not None:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = self._VALID_DRINKS[drink_type](name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type not in self._VALID_TABLES:
            return None

        if self._find_table(table_number) is not None:
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = self._VALID_TABLES[table_type](table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = next((x for x in self.tables_repository if x.capacity >= number_of_people and not x.is_reserved), None)
        if table is None:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_item(self, table_number: int, *items, item_type: str):
        table = self._find_table(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        menu_attrs, orders_attrs = self._ORDER_ATTRS[item_type]
        menu = getattr(self, menu_attrs)
        table_order = getattr(table, orders_attrs)
        ordered, unavailable = [], []

        for item in items:
            product = next((x for x in menu if x.name == item), None)
            if product is None:
                unavailable.append(item)
            else:
                ordered.append(str(product))
                table_order.append(product)

        res = [f"Table {table_number} ordered:", *ordered, f"{self.name} does not have in the menu:", *unavailable]

        return "\n".join(res)

    def order_food (self, table_number: int, *food_names):
        return self.order_item(table_number, *food_names, item_type="Food")

    def order_drink(self, table_number: int, *drinks):
        return self.order_item(table_number, *drinks, item_type="Drink")

    def leave_table(self, table_number: int):
        table = self._find_table(table_number)
        if table is None:
            return None

        bill = table.get_bill()
        table.clear()
        self.total_income += bill
        return "\n".join([f"Table: {table_number}", f"Bill: {bill:.2f}"])

    def get_free_tables_info(self):
        res = [table.free_table_info() for table in self.tables_repository if not table.is_reserved]
        return "\n".join(res)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"