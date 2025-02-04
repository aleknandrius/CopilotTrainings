
import unittest
from datetime import date
from my_app.domain import Author, Book
from my_app.repository import BookRepository
from my_app.service import LibraryService

class TestLibraryService(unittest.TestCase):

    def setUp(self):
        self.book_repo = BookRepository()
        self.service = LibraryService(self.book_repo)
        author_1 = Author(author_id=1, name="Jane Austen", birthdate=date(1775, 12, 16))
        book_1 = Book(book_id=101, title="Pride and Prejudice", author=author_1, publication_year=1813)
        self.book_repo.add_book(book_1)

    def test_check_out_success(self):
        book = self.service.check_out_book(101)
        self.assertIsNotNone(book)
        self.assertTrue(book.is_checked_out)

    def test_check_out_nonexistent(self):
        book = self.service.check_out_book(999)
        self.assertIsNone(book)

    def test_return_book(self):
        # Check it out first
        self.service.check_out_book(101)
        result = self.service.return_book(101)
        self.assertTrue(result)
        # Make sure it's now available
        b = self.book_repo.find_by_id(101)
        self.assertFalse(b.is_checked_out)

if __name__ == '__main__':
    unittest.main()
