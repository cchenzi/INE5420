import numpy as np
from functools import reduce
from PyQt5 import QtGui

from app.utils import Shape
from app.math_functions import (
    transformations_functions_dict,
    build_homogeneous_coordinates,
    calculate_object_center,
    normalize_point,
    desnormalize_point,
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
        self.center = None
        self.normalization_values = normalization_values
        self.transform_coordinates()
        # self.normalize_and_transform_points(0)

    def convert_transformations(self):
        self.transformations = []
        for (code, params) in self.transformations_codes:
            print(code, params)
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
        return code in ["rt", "sc", "r_rt"]

    def normalize_points(self):
        self.normalized_coordinates = []
        for point in self.coordinates:
            self.normalized_coordinates.append(
                normalize_point(point, self.normalization_values)
            )

    def transform_coordinates(self):
        print("coord=", self.coordinates)
        self.normalize_points()
        print("normalized=", self.normalized_coordinates)
        coord_aux = build_homogeneous_coordinates(self.normalized_coordinates)
        for (code, params) in self.transformations_codes:
            t_aux = []
            if self.needs_translation(code):
                if code in ["rt", "r_rt"]:
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
<<<<<<< HEAD

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
=======
        print("tranformed=", self.transformed_coordinates)
>>>>>>> 2542e78 (Add window rotation)
