from unittest import TestCase, main
from project.library import Library


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.lib = Library('Pen')

    def test_constructor(self):
        self.assertEqual((self.lib.name, self.lib.books_by_authors, self.lib.readers), ('Pen', {}, {}))

    def test_name_empty_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.lib.name = ''

        self.assertEqual(str(ve.exception), "Name cannot be empty string!")

    def test_add_book(self):
        author = 'Horhe'
        title = '6th Seal'

        self.lib.add_book(author, title)

        res = self.lib.books_by_authors
        exp_res = {author: [title]}

        self.assertEqual(res, exp_res)

        self.lib.books_by_authors = {'Horhe': ['6th Seal']}
        new_book = 'Jimitelia'

        self.lib.add_book(author, new_book)

        res2 = self.lib.books_by_authors
        exp_res2 = {'Horhe': ['6th Seal', 'Jimitelia']}

        self.assertEqual(res2, exp_res2)

    def test_add_reader_already_registered(self):
        reader = 'Pen4o'
        self.lib.readers = {reader: []}

        message = self.lib.add_reader(reader)

        res = self.lib.readers
        exp_res = {reader: []}

        self.assertEqual(message, f"{reader} is already registered in the Pen library.")
        self.assertEqual(res, exp_res)

    def test_add_reader(self):
        reader = 'Pen4o'

        self.lib.add_reader(reader)

        res = self.lib.readers
        exp_res = {reader: []}

        self.assertEqual(res, exp_res)

    def test_rent_book_not_registered_user(self):
        self.lib.readers = {'Gan4o': []}
        reader = 'Pen4o'
        author = 'Horhe'
        title = 'The Book'

        message = self.lib.rent_book(reader, author, title)

        res = self.lib.readers
        exp_res = {'Gan4o': []}

        self.assertEqual(message, f"{reader} is not registered in the Pen Library.")
        self.assertEqual(res, exp_res)

    def test_rent_book_no_author(self):
        self.lib.books_by_authors = {'P.K Dick': 'Neuromancer'}
        self.lib.readers = {'Gan4o': []}
        reader = 'Gan4o'
        author = 'Horhe'
        title = 'The Book'

        message = self.lib.rent_book(reader, author, title)

        res = self.lib.readers
        exp_res = {'Gan4o': []}

        self.assertEqual(message, f"Pen Library does not have any {author}'s books.")
        self.assertEqual(res, exp_res)

    def test_rent_book_no_book(self):
        self.lib.books_by_authors = {'P.K Dick': 'Neuromancer'}
        self.lib.readers = {'Gan4o': []}
        reader = 'Gan4o'
        author = 'P.K Dick'
        title = 'Ubik'

        message = self.lib.rent_book(reader, author, title)

        res = self.lib.readers
        exp_res = {'Gan4o': []}

        self.assertEqual(message, f"""Pen Library does not have {author}'s "{title}".""")
        self.assertEqual(res, exp_res)

    def test_rent_book(self):
        self.lib.books_by_authors = {'P.K Dick': ['Neuromancer', 'Ubik']}
        self.lib.readers = {'Gan4o': []}
        reader = 'Gan4o'
        author = 'P.K Dick'
        title = 'Ubik'

        self.lib.rent_book(reader, author, title)

        res = self.lib.readers
        exp_res = {'Gan4o': [{'P.K Dick': 'Ubik'}]}

        self.assertEqual(res, exp_res)
        self.assertEqual(self.lib.books_by_authors, {'P.K Dick': ['Neuromancer']})


if __name__ == '__main__':
    main()