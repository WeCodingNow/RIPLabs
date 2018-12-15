from LabPythonOOP.abstract_colour import Colour
from LabPythonOOP.abstract_figure import Figure


class Circle(Figure):
    def __init__(self, radius=0, colour="red"):
        self._radius = radius
        self.colour = colour(colour)
        self.name = "круг"

    def surface(self):
        from math import pi
        return pi * self._radius**2

    def get_name(self):
        return self.name

    def __repr__(self):
        return f"{self.get_name()} радиуса {self._radius}, с площадью {self.surface()}, цвет {self.colour}"
