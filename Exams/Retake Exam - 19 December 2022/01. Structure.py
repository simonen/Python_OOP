from typing import List
from project.band_members.musician import Musician
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.band import Band
from project.concert import Concert
from project.concert_tracker_app import ConcertTrackerApp


from project.concert_tracker_app import ConcertTrackerApp

musician_types = ["Singer", "Drummer", "Guitarist"]
names = ["George", "Alex", "Lilly"]

app = ConcertTrackerApp()

for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[0].learn_new_skill("sing low pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[1].learn_new_skill("play the drums with drum brushes"))
print(app.musicians[2].learn_new_skill("play rock"))
print(app.musicians[2].learn_new_skill("play jazz"))

print(app.create_band("RockName"))
for i in range(3):
    print(app.add_musician_to_band(names[i], "RockName"))
print('---------')
# print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))
print(app.create_concert("Jazz", 20, 5.20, 56.7, "Sofia"))
# print(app.remove_musician_from_band('Alex', "RockName"))
print('/**********')
print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))
# print(Concert.concertz['Rock'])
# print(list(map(lambda a: a.skills, app.bands[0].members)))
# print(app.bands[0])