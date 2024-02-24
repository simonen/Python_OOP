from unittest import TestCase, main
from project.bookstore import Bookstore


class BookstoreTest(TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(300)

    def test_constructor(self):
        book_limit = self.store.books_limit
        availability = self.store.availability_in_store_by_book_titles
        sold = self.store.total_sold_books

        res = book_limit, availability, sold
        exp_res = 300, {}, 0

        self.assertEqual(res, exp_res)

    def test_book_limit_zero_or_less_exc(self):
        limit_value = 0
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = limit_value

        self.assertEqual(f"Books limit of 0 is not valid", str(ve.exception))

    def test_len_override(self):
        self.store.availability_in_store_by_book_titles = {'A': 10, 'B': 2, 'C': 21, 'D': 3}
        res = len(self.store)
        exp_res = 36

        self.assertEqual(res, exp_res)

    def test_receive_book_limit_reach_exc(self):
        self.store.availability_in_store_by_book_titles = {'A': 1, 'B': 2, 'C': 1, 'D': 2}
        self.store.books_limit = 10
        book_title = 'Trial'
        number = 5
        with self.assertRaises(Exception) as ex:
            self.store.receive_book(book_title, number)

        res = self.store.availability_in_store_by_book_titles
        exp_res = {'A': 1, 'B': 2, 'C': 1, 'D': 2}

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertEqual(res, exp_res)
        self.assertEqual(self.store.books_limit, 10)

    def test_receive_book_not_present(self):
        self.store.availability_in_store_by_book_titles = {'A': 1, 'B': 2, 'C': 1, 'D': 2}
        book_title = 'Trial'
        number = 10

        message = self.store.receive_book(book_title, number)

        res = self.store.availability_in_store_by_book_titles
        exp_res = {'A': 1, 'B': 2, 'C': 1, 'D': 2, 'Trial': 10}

        self.assertEqual(message, f"{number} copies of {book_title} "
                                  f"are available in the bookstore.")
        self.assertEqual(res, exp_res)

    def test_receive_book_present_book(self):
        self.store.availability_in_store_by_book_titles = {'A': 1, 'B': 2, 'C': 1, 'D': 2}
        book_title = 'A'
        number = 10

        message = self.store.receive_book(book_title, number)

        res = self.store.availability_in_store_by_book_titles
        exp_res = {'A': 11, 'B': 2, 'C': 1, 'D': 2}

        self.assertEqual(message, f"11 copies of A "
                                  f"are available in the bookstore.")
        self.assertEqual(res, exp_res)
        self.assertEqual(self.store.books_limit, 300)

    def test_sell_book_no_book_exc(self):
        self.store.availability_in_store_by_book_titles = {'A': 1, 'B': 2, 'C': 1, 'D': 2}
        book_title = 'QQ'
        number = 10

        with self.assertRaises(Exception) as ex:
            self.store.sell_book(book_title, number)

        res = self.store.availability_in_store_by_book_titles
        exp_res = {'A': 1, 'B': 2, 'C': 1, 'D': 2}

        self.assertEqual(f"Book {book_title} doesn't exist!", str(ex.exception))
        self.assertEqual(res, exp_res)
        self.assertEqual(self.store.total_sold_books, 0)

    def test_sell_book_not_copies_exc(self):
        self.store.availability_in_store_by_book_titles = {'A': 1, 'B': 2, 'C': 1, 'D': 2}
        book_title = 'A'
        number = 10

        with self.assertRaises(Exception) as ex:
            self.store.sell_book(book_title, number)

        res = self.store.availability_in_store_by_book_titles
        exp_res = {'A': 1, 'B': 2, 'C': 1, 'D': 2}

        self.assertEqual(str(ex.exception), f"A has not enough copies to sell. Left: 1")
        self.assertEqual(res, exp_res)
        self.assertEqual(self.store.total_sold_books, 0)

    def test_sell_book(self):
        self.store.availability_in_store_by_book_titles = {'A': 21, 'B': 2, 'C': 1, 'D': 2}
        book_title = 'A'
        number = 10

        self.store.sell_book(book_title, number)
        message = self.store.sell_book(book_title, number)

        res = self.store.availability_in_store_by_book_titles
        exp_res = {'A': 1, 'B': 2, 'C': 1, 'D': 2}

        self.assertEqual(message, f"Sold {number} copies of {book_title}")
        self.assertEqual(res, exp_res)
        self.assertEqual(self.store.total_sold_books, 20)

    def test_str_override(self):
        self.store.availability_in_store_by_book_titles = {'A': 11, 'B': 0}

        self.store.__total_sold_books = 10
        sold = self.store.total_sold_books

        res = str(self.store)
        exp_res = f"Total sold books: {sold}" \
                  f"\nCurrent availability: 11" \
                  f"\n - A: 11 copies" \
                  f"\n - B: 0 copies" \


        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    main()