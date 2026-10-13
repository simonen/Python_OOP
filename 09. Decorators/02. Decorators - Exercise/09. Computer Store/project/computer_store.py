from project.computer_store_app import ComputerStoreApp


computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", " ", "Gibiiiten", "Apple M1 Pro", 64))
print(f"{computer_store.warehouse=}", f"{computer_store.warehouse[0].price=}")
print(f"{computer_store.profits=}")
print(computer_store.sell_computer(10000, "Apple M1 Pro", 64))
print(computer_store.profits)
# print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))


print("    ".split())