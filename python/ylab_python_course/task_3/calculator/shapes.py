"""A module with classes geometric figures."""
from abc import ABC, abstractmethod
from math import sqrt, pi, sin, radians
from typing import Tuple


class Shape(ABC):
    """An abstact class for geometric figures."""

    def __init__(self, *args):
        """Create a Shape."""
        for arg in args:
            if arg <= 0:
                raise ValueError("Values must be positive.")

    @abstractmethod
    def get_area(self) -> float:
        """Calculate shape's area."""

    @abstractmethod
    def get_perimeter(self) -> float:
        """Calculate shape's perimeter."""


class Circle(Shape):
    """A class for circle."""

    def __init__(self, r: float):
        """Create a Cirle.

        Args:
            r: radius
        """
        super().__init__(r)
        self.r = r

    def get_area(self) -> float:
        """Calculate circle area."""
        return pi * self.r * self.r

    def get_perimeter(self) -> float:
        """Calculate circumference."""
        return 2 * pi * self.r


class Square(Shape):
    """A class for square."""

    def __init__(self, a: float):
        """Create a Square.

        Args:
            a: side length
        """
        super().__init__(a)
        self.a = a

    def get_area(self) -> float:
        """Calculate area."""
        return self.a ** 2

    def get_perimeter(self) -> float:
        """Calculate perimeter."""
        return self.a * 4


class Rectangle(Square):
    """A class for rectangle."""

    def __init__(self, a: float, b: float):
        """Create a Rectangle.

        Args:
            a: side length
            b: side length
        """
        Shape.__init__(a, b)
        self.a = a
        self.b = b

    def get_area(self) -> float:
        """Calculate rectangle area."""
        return self.a * self.b

    def get_perimeter(self) -> float:
        """Calculate rectangle perimeter."""
        return (self.a + self.b) * 2


class Triangle(Rectangle):
    """A class for triangle."""

    def __init__(self, a: float, b: float, c: float):
        """Create a Triangle.

        Args:
            a: side length
            b: side length
            c: side length
        """
        self.validate_sides(a, b, c)
        Shape.__init__(a, b, c)
        self.c = c

    @staticmethod
    def validate_sides(*sides: Tuple[float]):
        """Check for sides that are too long.

        Raises:
            ValueError: if a side is too long
        """
        for index, side in enumerate(sides):
            other_sides = sides[:index] + sides[index + 1 :]
            if side >= sum(other_sides):
                raise ValueError(
                    "Each side should be shorter than the sum of others."
                )

    def get_area(self) -> float:
        """Calculate triangle area."""
        hp = self.get_perimeter() / 2
        return sqrt(hp * (hp - self.a) * (hp - self.b) * (hp - self.c))

    def get_perimeter(self) -> float:
        """Calculate triangle perimeter."""
        return self.a + self.b + self.c


class Trapezoid(Triangle):
    """A class for trapezoid."""

    def __init__(self, a: float, b: float, c: float, d: float):
        """Create a Trapezoid.

        Args:
            a: base length
            b: base length
            c: side length
            d: side length
        """
        Shape.__init__(a, b, c, d)
        super().validate_sides(a, b, c, d)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_midline(self) -> float:
        """Calculate trapezoid midline."""
        return (self.a + self.b) / 2

    def get_height(self) -> float:
        """Calculate trapezoid height."""
        h = sqrt(
            self.c ** 2
            - (
                (self.a - self.b) ** 2
                + self.c ** 2
                - self.d ** 2 / 2 * (self.a - self.b)
            )
            ** 2
        )
        return h

    def get_area(self) -> float:
        """Calculate trapezoid area."""
        return self.get_height() * self.get_midline()

    def get_perimeter(self) -> float:
        """Calculate trapezoid perimeter."""
        return self.a + self.b + self.c + self.d


class Rhombus(Square):
    """A class for rhombus."""

    def __init__(self, a: float, angle: float):
        """Create a Rhombus.

        Args:
            a: side length
            angle: angle between sides (in degrees)
        """
        if angle >= 180:
            raise ValueError(
                "The rhombus angle must be less than 180 degrees."
            )
        Shape.__init__(a, angle)
        super().__init__(a)
        self.angle = angle

    def get_area(self) -> float:
        """Calculate area."""
        return self.a ** 2 * sin(radians(self.angle))


class Sphere(Circle):
    """A class for sphere."""

    def __init__(self, r: float):
        """Create a Sphere.

        Args:
            r: radius
        """
        # we only need this to change the docstring
        super().__init__(r)

    def get_area(self):
        """Calculate sphere's surface area."""
        return 4 * pi * self.r ** 2

    def get_volume(self):
        """Calculate sphere's volume."""
        return 4 / 3 * pi * self.r ** 3


class Cube(Square):
    """A class for cube."""

    def __init__(self, a: float):
        """Create a Cube.

        Args:
            a: edge length
        """
        # we only need this to change the docstring
        super().__init__(a)

    def get_perimeter(self) -> float:
        """Calculate cube's perimeter."""
        return 12 * self.a

    def get_area(self) -> float:
        """Calculate cube's surface area."""
        return 6 * self.a ** 2

    def get_volume(self) -> float:
        """Calculate cube's volume."""
        return self.a ** 3


class Parallelepiped(Rectangle):
    def __init__(self, a: float, b: float, c: float):
        """Create a rectangular cuboid Parallelepiped.

        Args:
            a: edge length
            b: edge length
            c: edge length
        """
        Shape.__init__(a, b, c)
        super().__init__(a, b)
        self.c = c

    def get_perimeter(self) -> float:
        """Calculate parallelepiped's perimeter."""
        return 4 * (self.a + self.b + self.c)

    def get_area(self) -> float:
        """Calculate parallelepiped's surface area."""
        return 2 * (self.a * self.b + self.b * self.c + self.c * self.a)

    def get_volume(self) -> float:
        """Calculate parallelepiped's volume."""
        return self.a * self.b * self.c


class Pyramid(Shape):
    def __init__(self, a: float):
        """Create a regular tetrahedron Pyramid.

        Args:
            a: edge length
        """
        super().__init__(a)
        self.a = a

    def get_perimeter(self) -> float:
        """Calculate pyramid's perimeter."""
        return 6 * self.a

    def get_area(self) -> float:
        """Calculate pyramid's surface area."""
        return sqrt(3) * self.a ** 2

    def get_volume(self) -> float:
        """Calculate pyramid's volume."""
        return self.a ** 3 / (6 * sqrt(2))

    def get_height(self) -> float:
        """Calculate pyramid's height."""
        return sqrt(2 / 3) * self.a


class Cylinder(Circle):
    def __init__(self, r: float, h: float):
        """Create a Cylinder.

        Args:
            r: base radius
            h: height
        """
        super().__init__(r)
        self.h = h

    def get_perimeter(self) -> float:
        """Calculate the perimeter of cylinder's base."""
        return super().get_perimeter(self)

    def get_area(self) -> float:
        """Calculate cylinders's surface area."""
        return 2 * pi * self.r * (self.h + self.r)

    def get_volume(self) -> float:
        """Calculate cylinders's volume."""
        return pi * self.r ** 2 * self.h


class Cone(Circle):
    def __init__(self, r: float, h: float):
        """Create a right circular Cone.

        Args:
            r: base radius
            h: height
        """
        Shape.__init__(r, h)
        super().__init__(r)
        self.h = h

    def get_perimeter(self) -> float:
        """Calculate the perimeter of the cone's base."""
        return super().get_perimeter()

    def get_slant_height(self) -> float:
        """Calculate the length of the cone's line."""
        return sqrt(self.r ** 2 + self.h ** 2)

    def get_area(self) -> float:
        """Calculate cone's surface area."""
        return pi * self.r * self.get_slant_height() + super().get_area()

    def get_volume(self) -> float:
        """Calculate cone's volume."""
        return 1 / 3 * pi * self.r ** 2 * self.h


SHAPES = {
    1: Circle,
    2: Square,
    3: Rectangle,
    4: Triangle,
    5: Trapezoid,
    6: Rhombus,
    7: Sphere,
    8: Cube,
    9: Parallelepiped,
    10: Pyramid,
    11: Cylinder,
    12: Cone,
}
