from .shape import Shape
from .visitor import Visitor

class Sphere(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def accept(self, visitor: Visitor):
        return visitor.visit_sphere(self) 