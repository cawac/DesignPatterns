import math

from geometry.Visitor import Visitor
from geometry.Sphere import Sphere
from geometry.Parallelepiped import Parallelepiped
from geometry.Torus import Torus
from geometry.Cube import Cube

class VolumeVisitor(Visitor):
    def visit_sphere(self, sphere: Sphere):
        return (4 / 3) * math.pi * sphere.radius ** 3

    def visit_parallelepiped(self, parallelepiped: Parallelepiped):
        return parallelepiped.length * parallelepiped.width * parallelepiped.height

    def visit_torus(self, torus: Torus):
        return (2 * math.pi ** 2) * torus.major_radius * torus.minor_radius ** 2

    def visit_cube(self, cube: Cube):
        return cube.edge ** 3
