import unittest
from book import Book
from bookshelf import BookShelf
from typing import List


class BookShelfTest(unittest.TestCase):
    _bookShelf: BookShelf
    _books: List[Book]

    def setUp(self) -> None:
        self._bookShelf = BookShelf()
        self._books = [
            Book("Isaac Asimov", "I, Robot"),
            Book("Ray Bradbury", "Fahrenheit 451"),
            Book("Ted Chiang", "Stories of Your Life and Others"),
        ]
        for book in self._books:
            self._bookShelf.append_book(book)

    def test_len(self):
        self.assertEqual(self._bookShelf.__len__(), 3)

    def test_iterator(self):
        for i, book in enumerate(self._bookShelf):
            self.assertEqual(book, self._books[i])

    def test_remove_at(self):
        self._bookShelf.remove_at(1)
        print(self._bookShelf._books)
        self.assertEqual(self._bookShelf.__len__(), 2)
        self.assertEqual(self._bookShelf.book_at(0), self._books[0])
        self.assertEqual(self._bookShelf.book_at(1), self._books[2])
        self._bookShelf.remove_at(0)
        self._bookShelf.remove_at(0)
        self.assertEqual(self._bookShelf.__len__(), 0)
