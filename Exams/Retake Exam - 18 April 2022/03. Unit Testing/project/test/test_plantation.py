from unittest import TestCase, main
from project.plantation import Plantation


class PlantationTest(TestCase):
    def setUp(self) -> None:
        self.plant = Plantation(10)

    def test_constructor(self):
        self.assertEqual((self.plant.size, self.plant.plants, self.plant.workers), (10, {}, []))

    def test_size_below_0_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.size = -1

        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_worker_already_hired_exc(self):
        self.plant.workers = ['Pen4o', 'Gan4o']
        with self.assertRaises(ValueError) as ve:
            self.plant.hire_worker('Pen4o')

        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test_hire_worker(self):
        worker = 'Pen4o'
        message = self.plant.hire_worker(worker)

        res = self.plant.workers
        exp_res = [worker]

        self.assertEqual(message, f"{worker} successfully hired.")
        self.assertEqual(res, exp_res)

    def test_len_override(self):
        self.plant.plants = {'Pen4o': ['Magnolia', 'Dracena'], 'Gana': ['Flowers']}

        res = len(self.plant)
        exp_res = 3

        self.assertEqual(res, exp_res)

    def test_planting_no_worker_exc(self):
        self.plant.workers = ['Pen4o', 'Gan4o']
        worker = 'Min4o'
        plant = 'Plant1'

        with self.assertRaises(ValueError) as ve:
            self.plant.planting(worker, plant)

        res = self.plant.plants
        exp_res = {}

        self.assertEqual(res, exp_res)
        self.assertEqual(str(ve.exception), f"Worker with name {worker} is not hired!")

    def test_planting_full_exc(self):
        self.plant.workers = ['Pen4o', 'Gan4o']
        self.plant.plants = {'Pen4o': ['Magnolia', 'Dracena'], 'Gan4o': ['Flowers']}
        self.plant.size = 3
        worker = 'Gan4o'
        plant = 'Plant1'

        with self.assertRaises(ValueError) as ve:
            self.plant.planting(worker, plant)

        res = self.plant.plants
        exp_res = {'Pen4o': ['Magnolia', 'Dracena'], 'Gan4o': ['Flowers']}

        self.assertEqual(res, exp_res)
        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test_planting_first_plant(self):
        self.plant.workers = ['Pen4o', 'Gan4o']
        self.plant.plants = {'Pen4o': ['Magnolia', 'Dracena']}
        worker = 'Gan4o'
        plant = 'Plant1'

        message = self.plant.planting(worker, plant)

        res = self.plant.plants
        exp_res = {'Pen4o': ['Magnolia', 'Dracena'], 'Gan4o': ['Plant1']}

        self.assertEqual(message, f"{worker} planted it's first {plant}.")
        self.assertEqual(res, exp_res)

    def test_planting(self):
        self.plant.workers = ['Pen4o', 'Gan4o']
        self.plant.plants = {'Pen4o': ['Magnolia', 'Dracena'], 'Gan4o': ['Mracena']}
        worker = 'Gan4o'
        plant = 'Plant1'

        message = self.plant.planting(worker, plant)

        res = self.plant.plants
        exp_res = {'Pen4o': ['Magnolia', 'Dracena'], 'Gan4o': ['Mracena', 'Plant1']}

        self.assertEqual(message, f"{worker} planted {plant}.")
        self.assertEqual(res, exp_res)

    def test_str_override(self):
        self.plant.workers = ['Pen4o', 'Gan4o']
        self.plant.plants = {'Pen4o': ['Magnolia', 'Dracena'], 'Gan4o': ['Mracena']}

        res = str(self.plant)
        exp_res = f"Plantation size: 10" \
                  f"\nPen4o, Gan4o" \
                  f"\nPen4o planted: Magnolia, Dracena" \
                  f"\nGan4o planted: Mracena"

        self.assertEqual(res, exp_res)

    def test_repr_override(self):
        self.plant.workers = ['Pen4o', 'Gan4o']

        res = self.plant.__repr__()
        exp_res = f'Size: 10' \
                  f'\nWorkers: Pen4o, Gan4o'

        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    main()