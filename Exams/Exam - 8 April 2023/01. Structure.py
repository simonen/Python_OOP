from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.robots_managing_app import RobotsManagingApp
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print('-' * 22)
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 10))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))
print(main_app.add_robot('FemaleRobot', 'Power', 'FunnyRobots', 41221.11))
print(main_app.add_robot('MaleRobot', 'Chugun', 'WarRobots', 1211.11))
print()
print(main_app.services[0].capacity)
print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Power', 'ServiceRobotsWorld'))
print(main_app.services[0].capacity)
print()
print(main_app.add_robot_to_service('Chugun', 'ServiceTechnicalsWorld'))
print()
print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))
print()
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))
print()
print(main_app)
print()
print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))
print(str(main_app))

print(main_app.services[0].capacity)
print(main_app.remove_robot_from_service('Power', 'ServiceRobotsWorld'))
