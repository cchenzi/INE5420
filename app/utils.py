from enum import Enum
from math_functions import x_viewport_transform, y_viewport_transform


class Shape(Enum):
    Nothing = 0
    Point = 1
    Line = 2
    Polygon = -1

    @classmethod
    def _missing_(cls, value):
        return Shape.Polygon


class CoordinatesRepresentation:
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.x_navigation = 0
        self.y_navigation = 0


def transform_coordinates(x, y, window_coordinates, viewport_coordinates):
    xvp = x_viewport_transform(
        x,
        window_coordinates.x_min,
        window_coordinates.x_max,
        viewport_coordinates.x_min,
        viewport_coordinates.x_max,
        viewport_coordinates.x_navigation,
    )
    yvp = y_viewport_transform(
        y,
        window_coordinates.y_min,
        window_coordinates.y_max,
        viewport_coordinates.y_min,
        viewport_coordinates.y_max,
        viewport_coordinates.y_navigation,
    )
    return (xvp, yvp)


def calculate_coordinate_shift(max_coordinate, min_coordinate, step):
    size = max_coordinate - min_coordinate
    return size * step
