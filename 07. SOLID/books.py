from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page: int) -> None:
        self.page = page


class Library:
    def __init__(self, name):
        self.name = name
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def find_book(self, title):
        try:
            book = next(x for x in self.books if x.title == title)
            return book.title
        except StopIteration:
            return f"Book '{title}' not found in '{self.name}' library."


library = Library('Biblioteka')
book1 = Book('Light Fantastic', 'Pratchett')
book2 = Book('Witches Abroad', 'Pratchett')
library.add_book(book1)
library.add_book(book2)
print(library.find_book('Light Fantastic'))
print(library.find_book('Light'))

# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page
