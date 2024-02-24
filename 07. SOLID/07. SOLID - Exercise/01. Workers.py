from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(Employee):
    def work(self):
        print("I'm working!!")


class SuperWorker(Employee):
    def work(self):
        print("I work very hard!!!")


class Bachker(Employee):
    def work(self):
        print('Bachkam qko')


class Boss:
    def work(self):
        print('I am the Boss!')


class Manager:

    def __init__(self):
        self.employee = None

    def set_worker(self, employee: Employee):
        if not isinstance(employee, Employee):
            raise AssertionError(f"Worker must be of type {Employee}")

        self.employee = employee

    def manage(self):
        if self.employee is not None:
            self.employee.work()


bacho = Bachker()
worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()
boss = Boss()
super_worker = SuperWorker()

try:
    manager.set_worker(boss)
    manager.manage()
except AssertionError:
    print(f"manager fails to support the given class....")
