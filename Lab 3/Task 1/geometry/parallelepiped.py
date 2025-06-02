from .shape import Shape
from .visitor import Visitor

class Parallelepiped(Shape):
    def __init__(self, height: float, width: float, length: float):
        self.height = height
        self.length = length
        self.width = width

    def accept(self, visitor: Visitor):
        return visitor.visit_parallelepiped(self)
