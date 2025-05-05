from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    author: str
    content: str
    is_restricted: bool = False 