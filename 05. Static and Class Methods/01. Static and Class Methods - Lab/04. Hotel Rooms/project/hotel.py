from project.room import Room


class Hotel:

    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        room = next(r for r in self.rooms if r.number == room_number)
        if room.take_room(people) is None:
            self.guests += people

        return room.take_room(people)

    def free_room(self, room_number):
        room = next(r for r in self.rooms if r.number == room_number)
        people = room.guests
        if room.free_room() is None:
            self.guests -= people

        return room.free_room()

    def status(self):
        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(map(str, free_rooms))}\n" \
               f"Taken rooms: {', '.join(map(str, taken_rooms))}"
