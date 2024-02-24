from project.bakery import Bakery

bakery = Bakery("Sunny")

print(f"{'# ADD_FOOD'}")
print(bakery.add_food("Bread", "Sour", 1.50))
print(bakery.add_food("Bread", "White", 1.30))
print(bakery.add_food("Cake", "Chocolate", 2.90))
print(bakery.add_food("Cake", "Vanilla", 2.90))

print(f"\n\n{'# ADD_DRINK'}")
print(bakery.add_drink("Water", "Spring", 250, "Bankya"))
print(bakery.add_drink("Water", "Mineral", 500, "Devin"))
print(bakery.add_drink("Tea", "Black", 250, "Ahmad Tea"))
print(bakery.add_drink("Tea", "Green", 250, "Lipton"))

print(f"\n\n{'# ADD_TABLE'}")
print(bakery.add_table("OutsideTable", 100, 9))
print(bakery.add_table("OutsideTable", 95, 15))
print(bakery.add_table("InsideTable", 1, 15))
print(bakery.add_table("InsideTable", 4, 15))

print(f"\n\n{'# RESERVE_TABLE'}")
print(bakery.reserve_table(12))
print(bakery.reserve_table(12))
print(bakery.reserve_table(12))
# print(bakery.reserve_table(9))
table95 = next(t for t in bakery.tables_repository if t.table_number == 95)
table1 = next(t for t in bakery.tables_repository if t.table_number == 1)
table4 = next(t for t in bakery.tables_repository if t.table_number == 4)
table100 = next(t for t in bakery.tables_repository if t.table_number == 100)
print(table100)
print(table95)
print(table1)
print(table4)
print(f"\n\n{'# ORDERS_FOOD'}")
print(bakery.order_food(95, "Sour", "White", "Chocolate", "Vanilla", "Strawberry", "Hazelnut", "Wholegrain"))
print(bakery.order_food(34, "Sour", "Strawberry", "Hazelnut", "Wholegrain"))
print(bakery.order_food(1, "Sour", "Strawberry", "Hazelnut", "Wholegrain"))

print(f"\n\n{'# ORDERS_DRINK'}")
print(bakery.order_drink(95, "Spring", "Mineral", "Black", "Green", "White", "Tap", "Fruit"))
print(bakery.order_drink(4, "Spring", "Mineral", "Black", "Gisher", "White", "Tap", "Fruit"))
print(table95)
print(table100)
print(table1)
print(table4)
print(f"\n\n{'# LEAVE_TABLE'}")
print(bakery.leave_table(95))
print(bakery.leave_table(1))
print(bakery.leave_table(4))
print(table95)
print(table100)
print(table1)
print(table4)
#
print(f"\n\n{'# GET_TOTAL_INCOME'}")
print(bakery.get_total_income())
#
print(f"\n\n{'# TABLES_INFO'}")
print(bakery.reserve_table(12))
print(bakery.reserve_table(12))
print(bakery.reserve_table(12))
print(bakery.get_free_tables_info())
print(table100)
print(table4)
table4.reserve(4)
print(table4)

print(table4.free_table_info())
print()