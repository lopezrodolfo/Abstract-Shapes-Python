from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):
    PI = 3.14159

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @abstractmethod
    def area(self) -> None:
        pass

    @abstractmethod
    def perimeter(self) -> None:
        pass


class Polygon(Shape):

    def __str__(self):
        return "Polygon Shape " + super().__str__()

    @abstractmethod
    def area(self) -> None:
        pass

    @abstractmethod
    def perimeter(self) -> None:
        pass


class Oval(Shape):

    def __str__(self):
        return "Oval Shape " + super().__str__()

    @abstractmethod
    def area(self) -> None:
        pass

    @abstractmethod
    def perimeter(self) -> None:
        pass


class Rectangle(Polygon):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def __str__(self):
        return (
            super().__str__()
            + f" with an area of {self.area():.2f} and perimeter of {self.perimeter():.2f}"
        )

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __eq__(self, other):
        if self is other:
            return True
        elif isinstance(other, Rectangle):
            return self.area() == other.area()
        else:
            return False

    def __lt__(self, other):
        if self is other:
            return True
        elif isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return False


class Triangle(Polygon):
    def __init__(self, name, base, height, a, b, c):
        super().__init__(name)
        self.base = base
        self.height = height
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return (
            super().__str__()
            + f" with an area of {self.area():.2f} and perimeter of {self.perimeter():.2f}"
        )

    def area(self):
        return (self.base * self.height) / 2

    def perimeter(self):
        return self.a + self.b + self.c

    def __eq__(self, other):
        if self is other:
            return True
        elif isinstance(other, Triangle):
            return self.area() == other.area()
        else:
            return False

    def __lt__(self, other):
        if self is other:
            return True
        elif isinstance(other, Triangle):
            return self.area() < other.area()
        else:
            return False


class Ellipse(Oval):
    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b

    def __str__(self):
        return (
            super().__str__()
            + f" with an area of {self.area():.2f} and perimeter of {self.perimeter():.2f}"
        )

    def area(self):
        return Shape.PI * self.a * self.b

    def perimeter(self):
        return 2 * Shape.PI * (sqrt(self.a * self.a + self.b * self.b) / 2)

    def __eq__(self, other):
        if self is other:
            return True
        elif isinstance(other, Ellipse):
            return self.area() == other.area()
        else:
            return False

    def __lt__(self, other):
        if self is other:
            return True
        elif isinstance(other, Ellipse):
            return self.area() < other.area()
        else:
            return False


class Circle(Oval):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def __str__(self):
        return (
            super().__str__()
            + f" with an area of {self.area():.2f} and perimeter of {self.perimeter():.2f}"
        )

    def area(self):
        return Shape.PI * self.radius * self.radius

    def perimeter(self):
        return 2 * Shape.PI * self.radius

    def __eq__(self, other):
        if self is other:
            return True
        elif isinstance(other, Circle):
            return self.area() == other.area()
        else:
            return False

    def __lt__(self, other):
        if self is other:
            return True
        elif isinstance(other, Circle):
            return self.area() < other.area()
        else:
            return False
