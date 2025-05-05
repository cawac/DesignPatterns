from typing import Optional
from real_book import RealBook
from book_interface import IBook
from authentication_system import AUTH_SYSTEM


class BookProxy(IBook):
    def __init__(self, user_id: int):
        self._user_id = user_id
        self._authenticated = self._authenticate()
        self._real_book: Optional[RealBook] = None

    def get_book(self, book_id: int) -> Optional[RealBook]:
        if self._real_book and self._real_book.get_id() == book_id:
            return self._real_book

        if self._authenticated and self._can_access(book_id):
            self._get_real_book(book_id)
            print(f"User {self._user_id} have access to the book {book_id}.")

        return self._real_book

    def _authenticate(self) -> bool:
        if not AUTH_SYSTEM.is_user_registered(self._user_id):
            print("Access denied: User is not registered")
            return False

        return True

    def _can_access(self, book_id: int) -> bool:
        if not AUTH_SYSTEM.can_access_book(self._user_id, book_id):
            print("Access denied: User does not have permission to access this book")
            return False

        return True

    def _get_real_book(self, book_id: int) -> Optional[RealBook]:
        self._real_book = RealBook(book_id)
        return self._real_book

    def get_id(self) -> int:
        if self._real_book:
            return self._real_book.get_id()

        return -1

    def get_title(self) -> str:
        if self._real_book:
            return self._real_book.get_title()

        return ""

    def get_author(self) -> str:
        if self._real_book:
            return self._real_book.get_author()

        return ""

    def get_content(self) -> str:
        if self._real_book:
            return self._real_book.get_content()

        return ""