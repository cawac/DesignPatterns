from user import User


class AuthenticationSystem:
    def __init__(self):
        self._users = {
            1: User(1, "user1", {1, 3, 5}),
            2: User(2, "user2", {2, 4, 6}),
            3: User(3, "user3", set())
        }

    def is_user_registered(self, user_id: int) -> bool:
        user = self._users.get(user_id)
        return user is not None

    def can_access_book(self, user_id: int, book_id: int) -> bool:
        user = self._users.get(user_id)
        if not user:
            return False
        return book_id in user.allowed_book_ids


AUTH_SYSTEM = AuthenticationSystem()