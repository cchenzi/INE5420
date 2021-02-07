from enum import Enum


class Shape(Enum):
    POINT = 1
    LINE = 2
    TRIANGLE = 3
    SQUARE = 4
    PENTAGON = 5
    HEXAGON = 6
    HEPTAGON = 7
    OCTAGON = 8
    POLYGON = -1

    @classmethod
    def _missing_(cls, value):
        return Shape.POLYGON


class CoordinatesRepresentation:
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
