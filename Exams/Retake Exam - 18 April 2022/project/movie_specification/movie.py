from abc import ABC
from project.user import User


class Movie(ABC):
    _AGE_RESTRICTIONS = {"Action": 12, "Fantasy": 6, "Thriller": 16}
    _default_age_restriction: int | None = None

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        if cls.__name__ not in Movie._AGE_RESTRICTIONS:
            raise TypeError( f"{cls.__name__} is not in _AGE_RESTRICTIONS — "
            f"add it or set a default explicitly.")

        cls._default_age_restriction = Movie._AGE_RESTRICTIONS.get(cls.__name__)

    def __init__(self, title: str, year: int, owner: User, age_restriction: int | None = None) -> None:
        self.title = title
        self.year = year
        self.owner: User = owner
        if age_restriction is None:
            age_restriction = self._default_age_restriction
        self.age_restriction = age_restriction
        self.likes: int = 0

    def details(self) -> str:
        return (f"{self.__class__.__name__} - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, "
                f"Likes:{self.likes}, Owned by:{self.owner.username}")

    @property
    def age_restriction(self):
        return self._age_restriction

    @age_restriction.setter
    def age_restriction(self, value: int):
        if value < self._AGE_RESTRICTIONS[self.__class__.__name__]:
            raise ValueError(f"{self.__class__.__name__} movies must be restricted for audience under 16 years!")

        self._age_restriction = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")

        self._year = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if not value.split():
            raise ValueError("The title cannot be empty string!")

        self._title = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value: User):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")

        # if value.age < self.age_restriction:
        #     raise ValueError("Malak si brat")

        self._owner = value
