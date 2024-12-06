class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

my_circle = Circle(5)
print(my_circle.area())

class Circle(Shape):
    def area(self):
        return super().area() + 3.14 * (self.radius ** 2)
