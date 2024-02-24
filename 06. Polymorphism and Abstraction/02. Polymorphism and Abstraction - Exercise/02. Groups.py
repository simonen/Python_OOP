from typing import List


class Person:

    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"


class Group:

    def __init__(self, name: str, people: List[Person]) -> None:
        self.name = name
        self.people = people

    def __add__(self, other):
        extended_group = self.people + other.people
        return Group(f"{self.name + ' ' + other.name}", extended_group)

    def __len__(self) -> int:
        return len(self.people)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.people):
            raise StopIteration

        person = self.people[self.index]
        person_string = f"Person {self.index}: {person.name + ' ' + person.surname}"
        self.index += 1

        return person_string

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item]}"

    def __repr__(self) -> str:
        return f"Group {self.name} with members {', '.join(map(str, self.people))}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3
first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group
print(len(first_group))
print(second_group)
print(third_group[0])
print()
for person in third_group:
    print(person)
