from geometry.Sphere import Sphere
from geometry.Parallelepiped import Parallelepiped
from geometry.Torus import Torus
from geometry.Cube import Cube
from VolumeVisitor import VolumeVisitor


def main():
    shapes = [
        Sphere(radius=3),
        Parallelepiped(length=2, width=4, height=6),
        Torus(major_radius=5, minor_radius=1),
        Cube(edge=4)
    ]

    visitor = VolumeVisitor()

    for shape in shapes:
        volume = shape.accept(visitor)
        print(f"{shape.__class__.__name__} volume: {volume:.2f}")

if __name__ == "__main__":
    main()
