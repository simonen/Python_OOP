from project.robot import Robot
from unittest import TestCase, main


class RobotTest(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("T1000", "Military", 10, 1299)

    def test_constructor(self):
        robot_id = self.robot.robot_id
        robot_cat = self.robot.category
        robot_cap = self.robot.available_capacity
        robot_price = self.robot.price

        res = (robot_id, robot_cat, robot_cap, robot_price)
        exp_res = ('T1000', 'Military', 10, 1299)

        self.assertEqual(res, exp_res)

    def test_category_not_allowed_raise_exc(self):
        expected_cat = ['Military', 'Education', 'Entertainment', 'Humanoids']
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'NONE'

        self.assertEqual(f"Category should be one of '{expected_cat}'", str(ve.exception))

    def test_price_negative_raise_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_fail(self):
        hardware_component = 'Laser drill'
        self.robot.hardware_upgrades = ['Rockets', 'Laser drill']
        price = self.robot.price

        message = self.robot.upgrade(hardware_component, 10)

        res = self.robot.hardware_upgrades
        price_res = self.robot.price
        exp_res = ['Rockets', 'Laser drill']

        self.assertEqual(res, exp_res)
        self.assertEqual(price_res, 1299)
        self.assertEqual(message, f"Robot {self.robot.robot_id} was not upgraded.")

    def test_upgrade(self):
        hardware_component = 'Laser drill'
        self.robot.hardware_upgrades = ['Rockets']
        component_price = 10
        price = self.robot.price

        message = self.robot.upgrade(hardware_component, component_price)

        res = self.robot.hardware_upgrades
        price_res = self.robot.price
        exp_price = price + component_price * 1.5
        exp_res = ['Rockets', 'Laser drill']

        self.assertEqual(res, exp_res)
        self.assertEqual(price_res, exp_price)
        self.assertEqual(message, 'Robot T1000 was upgraded with Laser drill.')

    def test_update_fail(self):
        self.robot.software_updates = [1, 2.2, 3]

        message = self.robot.update(3, 1)

        soft_updates_res = self.robot.software_updates
        exp_soft_updates_res = [1, 2.2, 3]
        capacity_res = self.robot.available_capacity
        exp_capacity = 10

        self.assertEqual(message, "Robot T1000 was not updated.")
        self.assertEqual(soft_updates_res, exp_soft_updates_res)
        self.assertEqual(capacity_res, exp_capacity)

    def test_update(self):
        self.robot.software_updates = [1, 2.2, 3]

        message = self.robot.update(4, 1)

        soft_updates_res = self.robot.software_updates
        exp_soft_updates_res = [1, 2.2, 3, 4]
        capacity_res = self.robot.available_capacity
        exp_capacity = 10 - 1

        self.assertEqual(message, 'Robot T1000 was updated to version 4.')
        self.assertEqual(soft_updates_res, exp_soft_updates_res)
        self.assertEqual(capacity_res, exp_capacity)

    def test_gt_more_expensive(self):
        other = Robot('T900', "Military", 10, 800)

        message = self.robot.__gt__(other)

        self.assertEqual(message, 'Robot with ID T1000 is more expensive than Robot with ID T900.')

    def test_gt_equal_costs(self):
        other = Robot('T1900', "Military", 10, 1299)

        message = self.robot.__gt__(other)

        self.assertEqual(message, 'Robot with ID T1000 costs equal to Robot with ID T1900.')

    def test_gt_cheaper(self):
        other = Robot('T1900', "Military", 10, 1300)

        message = self.robot.__gt__(other)

        self.assertEqual(message, 'Robot with ID T1000 is cheaper than Robot with ID T1900.')


if __name__ == '__main__':
    main()