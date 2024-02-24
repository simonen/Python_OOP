from project.hotel import Hotel
from project.room import Room


hotel = Hotel.from_stars(5)
first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)
hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)
print(first_room.guests, first_room.is_taken, first_room.capacity)
first_room.take_room(4)
print(first_room.guests, first_room.is_taken, first_room.capacity)
hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
# print(hotel.status())

print(hotel.name)
print(hotel.rooms)

roomz = map(lambda x: x.number, hotel.rooms)
print(list(roomz))