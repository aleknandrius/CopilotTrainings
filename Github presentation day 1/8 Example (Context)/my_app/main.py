# main.py

from datetime import date
from domain import Author, Book
from repository import BookRepository
from service import LibraryService
from pprint import pprint

def seed_data(book_repo: BookRepository):
    """
    Populate the repository with sample data for demo.
    """
    author_1 = Author(author_id=1, name="Jane Austen", birthdate=date(1775, 12, 16))
    author_2 = Author(author_id=2, name="Mark Twain", birthdate=date(1835, 11, 30))

    book_repo.add_book(Book(book_id=101, title="Pride and Prejudice", author=author_1, publication_year=1813))
    book_repo.add_book(Book(book_id=102, title="Emma", author=author_1, publication_year=1815))
    book_repo.add_book(Book(book_id=201, title="Adventures of Huckleberry Finn", author=author_2, publication_year=1884))

def main():
    book_repo = BookRepository()
    service = LibraryService(book_repo)
    seed_data(book_repo)

    # Show all books
    for book in book_repo.list_all_books():
        pprint(vars(book))

    # Check out a book
    checked_out = service.check_out_book(101)
    if checked_out:
        print(f"Checked out book: {checked_out.title}")
    else:
        print("Book not available.")

    # Attempt to check it out again
    second_try = service.check_out_book(101)
    print("Second try result:", second_try)

if __name__ == "__main__":
    main()
