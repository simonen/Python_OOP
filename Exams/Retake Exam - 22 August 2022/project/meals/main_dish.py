from project.meals.meal import Meal


class MainDish(Meal):

    def details(self):
        return f"Main Dish {self.name}: {self.price:.2f}lv/piece"
