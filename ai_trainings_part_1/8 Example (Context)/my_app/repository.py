# repository.py

from typing import Optional, List
from domain import Book, Author

class BookRepository:
    """
    Stores all books in an in-memory list.
    """

    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def find_by_id(self, book_id: int) -> Optional[Book]:
        for b in self._books:
            if b.book_id == book_id:
                return b
        return None

    def list_books_by_author(self, author: Author) -> List[Book]:
        return [b for b in self._books if b.author.author_id == author.author_id]

    def list_all_books(self) -> List[Book]:
        return self._books
