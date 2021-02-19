import numpy as np
from functools import reduce

from app.utils import Shape
from app.math_functions import transformations_functions_dict


class Wireframe:
    def __init__(self, coordinates, index, color):
        self.coordinates = coordinates
        self.number_points = len(self.coordinates)
        ones = np.ones((self.number_points, 1))
        self.homogeneous_coordinates = np.hstack((self.coordinates, ones))
        self.polygon_type = Shape(self.number_points).name
        self.name = f"{self.polygon_type}_{index}"
        self.color = color
        self.transformations = []
        self.transformations_codes = []
        self.transformed_coordinates = []
        self.apply_transformations_to_points()
        self.center = None
        self.calculate_object_center()

    def convert_transformations(self):
        self.transformations = []
        for (code, params) in self.transformations_codes:
            self.transformations.append(transformations_functions_dict[code](*params))

    def apply_transformations_to_points(self):
        self.convert_transformations()
        transformed_points = []
        for point in self.homogeneous_coordinates:
            transformed = reduce(np.dot, [point, *self.transformations])
            transformed_points.append((transformed[0], transformed[1]))

        self.transformed_coordinates = transformed_points

    def calculate_object_center(self):
        self.center = tuple(np.array(self.transformed_coordinates).mean(axis=0))
