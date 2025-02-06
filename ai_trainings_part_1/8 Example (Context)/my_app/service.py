# service.py

from typing import Optional
from domain import Book
from repository import BookRepository

class LibraryService:
    """
    Provides operations for checking books in/out, searching by author, etc.
    """

    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def check_out_book(self, book_id: int) -> Optional[Book]:
        """
        If the book is available, mark it as checked out and return it.
        Otherwise, return None if not found or already checked out.
        """
        book = self.book_repo.find_by_id(book_id)
        if book and not book.is_checked_out:
            book.is_checked_out = True
            return book
        return None

    def return_book(self, book_id: int) -> bool:
        """
        If the book is currently checked out, return it to the library (set is_checked_out=False).
        Returns True if successful, False otherwise.
        """
        book = self.book_repo.find_by_id(book_id)
        if book and book.is_checked_out:
            book.is_checked_out = False
            return True
        return False

    def list_books_by_author_name(self, author_name: str):
        """
        Return a list of books for any author matching 'author_name' (case-insensitive).
        """
        all_books = self.book_repo.list_all_books()
        return [
            b for b in all_books
            if b.author.name.lower() == author_name.lower()
        ]
