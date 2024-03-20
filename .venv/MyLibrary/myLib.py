from abc import ABC, abstractmethod
from math import pi

class Figure(ABC):
    @abstractmethod
    def square(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        if type(radius) not in [int, float]:
            raise TypeError("Radius must be an integer or float value")
        if radius < 0:
            raise ValueError("Radius must be not a negative value")
        self.radius = radius
    def square(self):
        return pi*self.radius*self.radius


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        return 0