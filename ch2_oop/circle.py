"""circle module: contains the Circle class """
import math


class Circle:
    """Circle Class"""
    all_circles = []
    pi = math.pi

    def __init__(self, r=1):
        self.radius = r
        Circle.all_circles.append(self)

    def area(self):
        return Circle.pi * self.radius ** 2

    @staticmethod
    def total_area():
        return sum(c.area() for c in Circle.all_circles)

    @classmethod
    def total_area1(cls):
        #benefit of using classmethod instead of static method is we dont have to hardcode the class name as in above
        return sum(c.area() for c in cls.all_circles)


obj = Circle(2)
print(obj.area())

obj2 = Circle(3)
print(obj2.area())
print(obj.total_area1())
