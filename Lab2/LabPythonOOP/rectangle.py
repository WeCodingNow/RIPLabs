from LabPythonOOP.abstract_colour import Colour
from LabPythonOOP.abstract_figure import Figure


class Rectangle(Figure):
    def __init__(self, width=0, height=0, colour="red"):
        self._width = width
        self._height = height
        self.colour = Colour(colour)
        self.name = "Прямоугольник"

    def surface(self):
        return self._width * self._height

    def get_name(self):
        return self.name

    def __repr__(self):
        return f"{self.get_name()} ширины {self._width}, высоты {self._height}, с площадью {self.surface()}, цвет {self.colour}"
