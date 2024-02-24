class Book:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages


bible = Book('Revelations', 'John', 100)

print(bible.name, bible.author)