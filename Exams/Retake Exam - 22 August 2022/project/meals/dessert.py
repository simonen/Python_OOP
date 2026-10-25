from project.meals.meal import Meal


class Dessert(Meal):
    def details(self):
        return f"Dessert {self.name}: {self.price:.2f}lv/piece"
