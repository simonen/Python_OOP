from project.movie_specification.movie import Movie


class Thriller(Movie):

    AGE = 16

    def __init__(self, title: str, year: int, owner, age_restriction=AGE):
        super().__init__(title, year, owner, age_restriction)

    def details(self) -> str:
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.AGE:
            raise ValueError("Thriller movies must be restricted for audience under 16 years!")

        self.__age_restriction = value
