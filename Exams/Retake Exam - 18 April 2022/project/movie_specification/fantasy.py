from project.movie_specification.movie import Movie


class Fantasy(Movie):

    AGE = 6

    def __init__(self, title: str, year: int, owner: object, age_restriction=AGE):
        super().__init__(title, year, owner, age_restriction)

    def details(self) -> str:
        return f"Fantasy - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.AGE:
            raise ValueError("Fantasy movies must be restricted for audience under 6 years!")

        self.__age_restriction = value
