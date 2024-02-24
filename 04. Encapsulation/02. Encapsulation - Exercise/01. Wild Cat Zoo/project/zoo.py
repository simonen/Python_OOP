from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        try:
            worker = next(filter(lambda x: x.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        salaries = sum([x.salary for x in self.workers])
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        expense = sum([x.money_for_care for x in self.animals])
        if self.__budget >= expense:
            self.__budget -= expense
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        animal_classes = ['Lion', 'Tiger', 'Cheetah']
        res = [f"You have {len(self.animals)} animals"]

        for animal in animal_classes:
            animals = [x for x in self.animals if x.__class__.__name__ == animal]
            animals_names = map(str, animals)
            res.append(f"----- {len(animals)} {animal}s:")
            res.extend(animals_names)

        return '\n'.join(res)

    def workers_status(self) -> str:
        worker_classes = ['Keeper', 'Caretaker', 'Vet']
        res = [f"You have {len(self.workers)} workers"]

        for worker in worker_classes:
            workers = [x for x in self.workers if x.__class__.__name__ == worker]
            workers_names = map(str, workers)
            res.append(f"----- {len(workers)} {worker}s:")
            res.extend(workers_names)

        return '\n'.join(res)
