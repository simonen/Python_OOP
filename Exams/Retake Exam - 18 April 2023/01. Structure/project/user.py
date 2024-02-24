class User:
    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = 0
        self.is_blocked = False

    @staticmethod
    def is_valid(string) -> bool:
        if len(string.strip()) != 0:
            return True

        return False

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value) -> None:
        if not self.is_valid(value):
            raise ValueError("First name cannot be empty!")

        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value) -> None:
        if not self.is_valid(value):
            raise ValueError("Last name cannot be empty!")

        self.__last_name = value

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        if not self.is_valid(value):
            raise ValueError("Driving license number is required!")

        self.__driving_license_number = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("Users rating cannot be negative!")

        self.__rating = value

    def increase_rating(self) -> None:
        self.__rating += 0.5
        if self.rating > 10:
            self.__rating = 10

    def decrease_rating(self) -> None:
        self.__rating -= 2.0
        if self.rating < 0:
            self.is_blocked = True
            self.__rating = 0

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} Driving license: {self.driving_license_number} Rating: {self.rating}"
