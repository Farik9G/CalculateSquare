from MyLibrary.Figure import Figure
from Exceptions.TriangleValueValidationException import TriangleValueError
from Exceptions.TriangleTypeValidationException import TriangleTypeError
from math import sqrt

class Triangle(Figure):
    def __init__(self, a, b, c):
        if not all(isinstance(side, (int, float)) and side != True for side in [a, b, c]):
            raise TriangleTypeError("Triangle sides must be an integer or float values")
        if a <= 0 or b <= 0 or c <= 0:
            raise TriangleValueError("Triangle sides must be not a negative values")
        if a + b <= c or a + c <= b or b + c <= a:
            raise TriangleValueError("A triangle with these sides doesn't exist")
        self.a = a
        self.b = b
        self.c = c

    def isRectangular(self):
        maxSide = max(self.a, self.b, self.c)
        if maxSide == self.a:
            return self.a * self.a == self.b * self.b + self.c * self.c
        elif maxSide == self.b:
            return self.b * self.b == self.a * self.a + self.c * self.c
        else:
            return self.c * self.c == self.a * self.a + self.b * self.b

    def square(self):
        p = (self.a + self.b + self.c)/2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


