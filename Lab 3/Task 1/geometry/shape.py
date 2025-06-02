from abc import ABC, abstractmethod

from .visitor import Visitor

class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass
