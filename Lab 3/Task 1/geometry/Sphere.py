from .Shape import Shape
from .Visitor import Visitor

class Sphere(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def accept(self, visitor: Visitor):
        return visitor.visit_sphere(self) 