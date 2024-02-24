from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.christmas_pastry_shop_app import ChristmasPastryShopApp


# bread = Gingerbread('Hlqp', 2.25)
# stolen = Stolen('MOlen', 3.05)
# print(bread.details())
# print(stolen.details())
#
# booth = OpenBooth(1, 10)
# booth.reserve(5)
# print(booth.is_reserved)
# print(booth.price_for_reservation)

shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.add_delicacy("Stolen", "Cake", 15.20))
print(shop.delicacies[0].details())
print(shop.delicacies[1].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.get_income())
print(shop.booths[0])
print(shop.reserve_booth(30))
print(shop.reserve_booth(30))
print(shop.booths[0])
print(shop.order_delicacy(1, "Gingy"))
print(shop.booths[0])
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Cake"))
print(shop.booths[0])
print(shop.booths[1])
print(shop.leave_booth(1))
print(shop.leave_booth(10))
print(shop.leave_booth(10))
print(shop.get_income())
print(shop.booths[0])
print(shop.booths[1])