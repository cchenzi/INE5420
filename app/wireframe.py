import numpy as np
from functools import reduce
from PyQt5 import QtGui

from app.utils import Shape
from app.math_functions import (
    transformations_functions_dict,
    build_homogeneous_coordinates,
    calculate_object_center,
    multiply_coordinates_by_transformations,
)


class Wireframe:
    def __init__(self, coordinates, index, color, normalization_values):
        self.coordinates = coordinates
        self.number_points = len(self.coordinates)
        self.homogeneous_coordinates = build_homogeneous_coordinates(self.coordinates)
        self.polygon_type = Shape(self.number_points).name
        self.name = f"{self.polygon_type}_{index}"
        self.color = color
        self.transformations = []
        self.transformations_codes = []
        self.transformed_coordinates = []
        self.normalized_coordinates = []
        self.normalization_values = normalization_values
        self.window_angle = 0
        self.window_x_shift_acc = 0
        self.window_y_shift_acc = 0
        self.window_transformations = None
        self.build_window_normalizations()
        self.center = None
        self.transform_coordinates()

    def calculate_object_center(self):
        self.center = tuple(np.array(self.transformed_coordinates).mean(axis=0))

    def needs_translation(self, code):
        return code in ["rt", "sc"]

    def build_window_normalizations(self):

        translation_matrix = transformations_functions_dict["tr"](
            self.window_x_shift_acc, self.window_y_shift_acc
        )

        rotation_matrix = transformations_functions_dict["rt"](self.window_angle)

        width = (self.normalization_values.x_max - self.normalization_values.x_min) / 2
        height = (self.normalization_values.y_max - self.normalization_values.y_min) / 2
        scaling_matrix = transformations_functions_dict["sc"](1 / width, 1 / height)

        composition = reduce(
            np.dot, [translation_matrix, rotation_matrix, scaling_matrix]
        )

        self.window_transformations = composition

    def transform_coordinates(self):
        coord_aux = build_homogeneous_coordinates(self.coordinates)
        coord_aux = multiply_coordinates_by_transformations(
            coord_aux, self.window_transformations
        )
        for (code, params) in self.transformations_codes:
            t_aux = []
            if self.needs_translation(code):
                if code in ["rt"]:
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

            composition_matrix = reduce(np.dot, t_aux)
            coord_aux = multiply_coordinates_by_transformations(
                coord_aux, composition_matrix
            )

        self.center = calculate_object_center(coord_aux)
        # Remove last column and map the points to tuple
        self.transformed_coordinates = list(map(tuple, coord_aux[:, :-1]))

    def to_obj(self):
        obj_list = []
        mtl_list = []

        obj_list.append(f'o {self.name}')
        obj_list.append(f'usemtl {self.name}_mtl')

        for vertex in self.transformed_coordinates:
            obj_list.append(f'v {vertex[0]} {vertex[1]} 0.0')

        f = ['f']
        points = [f'-{n+1}' for n in range(self.number_points)]
        f += points[::-1]
        f_line = ' '.join(f)
        obj_list.append(f_line)

        mtl_list.append(f'newmtl {self.name}_mtl')
        r, g, b, a = (0, 0, 0, 0)
        try:
            r, g, b, a = self.color.getRgb()
        except AttributeError:
            r, g, b, a = QtGui.QColor(self.color).getRgb()
        mtl_list.append(f'Kd {r/255} {g/255} {b/255} {a/255}')

        obj_list = [obj + '\n' for obj in obj_list]
        mtl_list = [mtl + '\n' for mtl in mtl_list]
        return (obj_list, mtl_list)