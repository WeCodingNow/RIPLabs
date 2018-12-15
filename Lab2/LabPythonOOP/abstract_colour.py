class Colour:
    def __init__(self, colour=None):
        self._colour = colour

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        self._colour = value

    @colour.deleter
    def colour(self):
        del self._colour

    def __repr__(self):
        return f"{self.colour}"
