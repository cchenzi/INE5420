import numpy as np
from functools import reduce

from app.utils import Shape
from app.math_functions import (
    transformations_functions_dict,
    build_homogeneous_coordinates,
    calculate_object_center,
)


class Wireframe:
    def __init__(self, coordinates, index, color):
        self.coordinates = coordinates
        self.number_points = len(self.coordinates)
        self.homogeneous_coordinates = build_homogeneous_coordinates(self.coordinates)
        self.polygon_type = Shape(self.number_points).name
        self.name = f"{self.polygon_type}_{index}"
        self.color = color
        self.transformations = []
        self.transformations_codes = []
        self.transformed_coordinates = []
        self.center = None
        self.apply_transformations_to_points()

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

    def needs_translation(self, code):
        return code in ["rt", "sc"]

    def transform_coordinates(self):
        coord_aux = build_homogeneous_coordinates(self.coordinates)
        for (code, params) in self.transformations_codes:
            t_aux = []
            if self.needs_translation(code):
                if code == "rt":
                    if len(params[1]) > 0:
                        translate_x, translate_y = params[1]
                    else:
                        translate_x, translate_y, _ = calculate_object_center(coord_aux)
                    params = [params[0]]
                else:
                    translate_x, translate_y, _ = calculate_object_center(coord_aux)
                t_aux.append(
                    transformations_functions_dict["tr"](-translate_x, -translate_y)
                )
                t_aux.append(transformations_functions_dict[code](*params))
                t_aux.append(
                    transformations_functions_dict["tr"](translate_x, translate_y)
                )
            else:
                t_aux.append(transformations_functions_dict[code](*params))
            transformed_points = []
            for point in coord_aux:
                transformed_points.append(tuple(reduce(np.dot, [point, *t_aux])))
            coord_aux = np.array(transformed_points)

        self.center = calculate_object_center(coord_aux)
        # Remove last column and map the points to tuple
        self.transformed_coordinates = list(map(tuple, coord_aux[:, :-1]))
