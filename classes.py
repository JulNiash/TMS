# classes.py

class InvalidPriceError(Exception):
    """Исключение, вызываемое при недопустимой цене книги."""
    pass

class InvalidYearError(Exception):
    """Исключение, вызываемое при недопустимом годе издания книги."""
    pass

class InvalidPagesError(Exception):
    """Исключение, вызываемое при недопустимом количестве страниц книги."""
    pass

from dataclasses import dataclass, field
from typing import List

@dataclass
class Book:
    pages: int
    year: int
    author: str
    price: float
    book_id: int = None

    def __post_init__(self):
        if self.price < 0:
            raise InvalidPriceError("price can't be less than 0")
        if self.year < 0:
            raise InvalidYearError("year can't be less than 0")
        if self.pages <= 0:
            raise InvalidPagesError("number of pages can't be less or equal to 0")

    def compare_price(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        if self.price < other.price:
            return f"{self.author}'s book is cheaper than {other.author}'s book."
        elif self.price > other.price:
            return f"{self.author}'s book is more expensive than {other.author}'s book."
        else:
            return f"{self.author}'s book and {other.author}'s book have the same price."

@dataclass
class Library:
    list_of_books: List[Book] = field(default_factory=list)
    counter: int = 0

    def add_book(self, pages, year, author, price):
        try:
            book = Book(book_id=self.counter, pages=pages, year=year, author=author, price=price)
            self.list_of_books.append(book)
            self.counter += 1
        except (InvalidPriceError, InvalidYearError, InvalidPagesError) as e:
            print(f"Adding error: {e}")

    def get_book_info(self, book_id):
        for book in self.list_of_books:
            if book.book_id == book_id:
                return f"ID: {book.book_id}, Author: {book.author}, Pages: {book.pages}, Year: {book.year}, Price: {book.price}"
        return "Book not found"

    def find_books_by_author(self, *args) -> List[Book]:
        return [book for book in self.list_of_books if book.author in args]
