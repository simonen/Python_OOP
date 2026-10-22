from project.movie_specification.movie import Movie
from project.movie_specification.thriller import Thriller
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: list[Movie] = []
        self.users_collection: list[User] = []

    def _find_user(self, username: str) -> User | None:
        return next((x for x in self.users_collection if x.username == username), None)

    def register_user(self, username: str, age: int) -> str:
        if self._find_user(username) is not None:
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self._find_user(username)
        if user is None:
            raise Exception("This user does not exist!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        if user is not movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self._find_user(username)
        if user is None:
            return None

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user is not movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for k, v in kwargs.items():
            setattr(movie, k, v)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self._find_user(username)
        if user is None:
            return None

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user is not movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self._find_user(username)
        if user is None:
            return None

        if user is movie.owner:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self._find_user(username)
        if user is None:
            return None

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        sorted_year_title = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        res = [x.details() for x in sorted_year_title]
        return "\n".join(res)

    def __str__(self):
        users = ', '.join([x.username for x in self.users_collection]) if self.users_collection else "No users."
        movies = ', '.join([x.title for x in self.movies_collection]) if self.movies_collection else "No movies."
        return f"All users: {users}" \
               f"\nAll movies: {movies}"