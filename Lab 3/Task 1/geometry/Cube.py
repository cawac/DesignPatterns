from .Shape import Shape
from .Visitor import Visitor

class Cube(Shape):
    def __init__(self, edge: float):
        self.edge = edge

    def accept(self, visitor: Visitor):
        return visitor.visit_cube(self) 