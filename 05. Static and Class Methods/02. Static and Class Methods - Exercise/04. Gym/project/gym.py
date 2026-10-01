from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer
from typing import TypeVar


T = TypeVar("T", Customer, Subscription, Trainer, Equipment, ExercisePlan)


class Gym:
    def __init__(self) -> None:
        self.customers: list[Customer] = []
        self.trainers: list [Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def _find_by_id(self, item_id: int, store: list[T]) -> T | None:
        value = next((x for x in store if x.id == item_id), None)
        return value

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        sub = self._find_by_id(subscription_id, self.subscriptions)
        plan = self._find_by_id(sub.exercise_id, self.plans)
        customer = self._find_by_id(sub.customer_id, self.customers)
        trainer = self._find_by_id(sub.trainer_id, self.trainers)
        equipment = self._find_by_id(plan.equipment_id, self.equipment)
        res = [sub, customer, trainer, equipment, plan]

        return "\n".join(map(str, res))