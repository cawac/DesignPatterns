from dataclasses import dataclass
from typing import Set

@dataclass
class User:
    id: int
    username: str
    allowed_book_ids: Set[int]