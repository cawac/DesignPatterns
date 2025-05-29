from abc import ABC, abstractmethod

from .Visitor import Visitor

class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass
