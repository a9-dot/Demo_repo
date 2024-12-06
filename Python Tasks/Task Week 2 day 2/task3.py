from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def print_area(shape):
    print(f"The area of the {shape.name} is {shape.area()}.")

# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)

print_area(circle)  # Output: The area of the Circle is 78.53981633974483.
print_area(rectangle)  # Output: The area of the Rectangle is 24.

