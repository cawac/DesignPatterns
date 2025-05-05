from book import Book
from book_interface import IBook

class RealBook(IBook):
    def __init__(self, book_id: int):
        self._book = self._load_book(book_id)

    def _load_book(self, book_id: int) -> Book:
        return Book(
            id=book_id,
            title=f"Book {book_id}",
            author=f"Author {book_id}",
            content=f"Content of book {book_id}",
            is_restricted=book_id % 2 == 0
        )

    def get_title(self) -> str:
        return self._book.title

    def get_author(self) -> str:
        return self._book.author

    def get_content(self) -> str:
        return self._book.content

    def get_id(self) -> int:
        return self._book.id 