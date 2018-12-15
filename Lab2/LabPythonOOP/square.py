from .rectangle import *


class Square(Rectangle):
    def __init__(self, side, colour="red"):
        super(Square, self).__init__(side, side, colour)
        self.name = "Квадрат"

    def get_name(self):
        return self.name

    def __repr__(self):
        return f"{self.get_name()} со стороной {self._width} и площадью {self.surface()}, цвет {self.colour}"
