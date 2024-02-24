from project.movie_specification.movie import Movie
from project.user import User
from typing import List


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int) -> str or None:
        if any(u for u in self.users_collection if u.username == username):
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie) -> str or None:
        user = next((u for u in self.users_collection if u.username == username), None)
        if not user:
            raise Exception("This user does not exist!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs) -> str or None:
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = next(u for u in self.users_collection if u.username == username)
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for k, v in kwargs.items():
            setattr(movie, k, v)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie) -> str or None:
        user = next(u for u in self.users_collection if u.username == username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie) -> str or None:
        user = next(u for u in self.users_collection if u.username == username)
        if user == movie.owner:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie) -> str or None:
        user = next(u for u in self.users_collection if u.username == username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self) -> str:
        if not self.movies_collection:
            return f"No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        return "\n".join(list(map(lambda x: x.details(), sorted_movies)))

    def __str__(self):
        users = ", ".join(list(map(lambda x: x.username, self.users_collection)))
        movies = ", ".join(list(map(lambda x: x.title, self.movies_collection)))

        return f"All users: {'No users.' if not self.users_collection else users}" \
               f"\nAll movies: {'No movies.' if not self.movies_collection else movies}"
