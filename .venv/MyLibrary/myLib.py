from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def square(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    def square(self):
        return 0

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        return 0