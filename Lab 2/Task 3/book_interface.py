from abc import ABC, abstractmethod

class IBook(ABC):
    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def get_author(self) -> str:
        pass

    @abstractmethod
    def get_content(self) -> str:
        pass

    @abstractmethod
    def get_id(self) -> int:
        pass 