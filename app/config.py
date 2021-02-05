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
