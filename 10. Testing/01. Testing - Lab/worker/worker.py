class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker('Ten4o', 1000, 100)

    def test_correct_name_salary_energy(self):
        name = self.worker.name
        salary = self.worker.salary
        energy = self.worker.energy

        res = name, salary, energy
        exp_res = 'Ten4o', 3000, 100
        self.assertEqual(res, exp_res)

    def test_rest(self):
        curr_energy = self.worker.energy
        self.worker.rest()
        res = self.worker.energy
        exp_res = curr_energy + 1
        self.assertEqual(res, exp_res)

    def test_work_no_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception.args[0]))

    def test_worker_money_increase(self):
        start_money = self.worker.money #0
        self.worker.work()
        res = self.worker.money
        exp_res = start_money + 1000
        self.assertEqual(res, exp_res)

    def test_worker_energy_decrease_work(self):
        starting_energy = self.worker.energy #100
        self.worker.work()
        res = self.worker.energy
        exp_res = starting_energy - 1
        self.assertEqual(exp_res, res)

    def test_get_info(self):
        res = self.worker.get_info()
        exp_res = 'Ten4o has saved 0 money.'
        self.assertEqual(exp_res, res)

if __name__ == '__main__':
    unittest.main()