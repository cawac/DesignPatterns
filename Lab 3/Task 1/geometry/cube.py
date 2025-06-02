from .shape import Shape
from .visitor import Visitor

class Cube(Shape):
    def __init__(self, edge: float):
        self.edge = edge

    def accept(self, visitor: Visitor):
        return visitor.visit_cube(self) 