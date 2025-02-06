# domain.py

from dataclasses import dataclass
from datetime import date

@dataclass
class Author:
    """
    Represents an author in our library system.
    """
    author_id: int
    name: str
    birthdate: date

@dataclass
class Book:
    """
    Represents a book in our library system.
    """
    book_id: int
    title: str
    author: Author
    publication_year: int
    is_checked_out: bool = False
