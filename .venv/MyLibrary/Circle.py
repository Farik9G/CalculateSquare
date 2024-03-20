from MyLibrary.Figure import Figure
from math import pi
from Exceptions.RadiusTypeValidationException import RadiusTypeError
from Exceptions.RadiusValueValidationException import RadiusValueError

class Circle(Figure):
    def __init__(self, radius):
        if type(radius) not in [int, float]:
            raise RadiusTypeError("Radius must be an integer or float value")
        if radius < 0:
            raise RadiusValueError("Radius must be not a negative value")
        self.radius = radius
    def square(self):
        return pi * self.radius * self.radius