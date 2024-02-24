class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

        self.__age = value

    def __str__(self):
        movies_liked = '\n'.join(list(map(lambda x: x.details(), self.movies_liked)))
        movies_owned = '\n'.join(list(map(lambda x: x.details(), self.movies_owned)))

        return f"Username: {self.username}, Age: {self.age}" \
               f"\nLiked movies:" \
               f"\n{'No movies liked.' if not self.movies_liked else movies_liked}" \
               f"\nOwned movies:" \
               f"\n{'No movies owned.' if not self.movies_owned else movies_owned}"
