from project.space_station import SpaceStation

station = SpaceStation()

print(f"\n\n# CREATING ASTRONAUTS")
print(station.add_astronaut('Biologist', 'B'))
print(station.add_astronaut('Biologist', 'B Senior'))
print(station.add_astronaut('Meteorologist', 'M'))
print(station.add_astronaut('Geodesist', 'G'))

print(f"\n\n# CREATING PLANETS")
print(station.add_planet('Mars', '1_item, 2_item, 3_item, 4_item, 5_item, 6_item', ))
print(station.add_planet('Earth', 'bananas'))
print(station.add_planet('Jupiter', 'stone, gems, sand,stone, gems, sand,stone, gems, sand'))
print(station.add_planet('Fail Planet', 'stone, gems, sand,stone, gems, sand,stone, gems, sand,stone, gems, sand,stone,'
                                        ' gems,sand,stone, gems, sand,stone, gems, sand,stone, gems, sand,stone, gems,'
                                        ' sand,stone, gems, sand,stone, gems, sand,stone, gems, sand'))
print(station.add_planet('Mars', 'stone'))

print(f"\n\n# RETIRE ASTRONAUT")
print(station.retire_astronaut('B Senior'))

print(f"\n\n# ASTRONAUTS INFO ")
for a in station.astronaut_repository.astronauts:
    print(a.oxygen, a.name, a.__class__.__name__)

print(f"\n\n# ASTRONAUTS INFO - AFTER RECHARGE")
station.recharge_oxygen()
for a in station.astronaut_repository.astronauts:
    print(a.oxygen, a.name, a.__class__.__name__)

print(f"\n\n# TEST SEND ON MISSION")
print(station.send_on_mission('Mars'))
print(station.send_on_mission('Jupiter'))
print(station.send_on_mission('Earth'))
print(station.send_on_mission('Fail Planet'))

print(f"\n\n# TEST REPORT")
station.add_astronaut('Biologist', 'Mr.Empty Backpack')
print(station.report())