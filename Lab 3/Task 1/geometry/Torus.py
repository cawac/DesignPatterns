from .Shape import Shape
from .Visitor import Visitor

class Torus(Shape):
    def __init__(self, major_radius: float, minor_radius: float):
        self.major_radius = major_radius
        self.minor_radius = minor_radius

    def accept(self, visitor: Visitor):
        return visitor.visit_torus(self)
