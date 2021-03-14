import numpy as np
from functools import reduce
from PyQt5 import QtGui

from app.utils import Shape
from app.math_functions import (
    transformations_functions_dict,
    build_homogeneous_coordinates,
    calculate_object_center,
    multiply_coordinates_by_transformations,
    normalize_point,
    calculate_bezier_points,
)


class Wireframe:
    def __init__(
        self, coordinates, index, color, normalization_values, window_transformations
    ):
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
        self.window_transformations = window_transformations
        self.window_width = (
            self.normalization_values.x_max - self.normalization_values.x_min
        )
        self.window_height = (
            self.normalization_values.y_max - self.normalization_values.y_min
        )
        self.center = None
        self.filled = False
        self.visible = True
        self.transform_coordinates()

    def calculate_object_center(self):
        self.center = tuple(np.array(self.transformed_coordinates).mean(axis=0))

    def needs_translation(self, code):
        return code in ["rt", "sc"]

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
                        translate_x, translate_y = normalize_point(
                            params[1], self.window_width / 2, self.window_height / 2
                        )
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
                if code == "tr":
                    x_normalized, y_normalized = normalize_point(
                        params, self.window_width / 2, self.window_height / 2
                    )
                    params = [x_normalized, y_normalized]
                t_aux.append(transformations_functions_dict[code](*params))

            composition_matrix = reduce(np.dot, t_aux)
            coord_aux = multiply_coordinates_by_transformations(
                coord_aux, composition_matrix
            )

        self.center = calculate_object_center(coord_aux)
        # Remove last column and map the points to tuple
        self.transformed_coordinates = list(map(tuple, coord_aux[:, :-1]))
        print("normalized coordinates=", self.transformed_coordinates)

    def to_obj(self, desnormalization_matrix):
        coord_aux = build_homogeneous_coordinates(self.transformed_coordinates)
        desnormalized_coordinates = multiply_coordinates_by_transformations(
            coord_aux, desnormalization_matrix
        )
        print(coord_aux, "->>>", desnormalization_matrix)
        obj_list = []
        mtl_list = []

        obj_list.append(f"o {self.name}")
        obj_list.append(f"usemtl {self.name}_mtl")

        for vertex in desnormalized_coordinates:
            obj_list.append(f"v {vertex[0]} {vertex[1]} 0.0")

        f = ["f"]
        points = [f"-{n+1}" for n in range(self.number_points)]
        f += points[::-1]
        f_line = " ".join(f)
        obj_list.append(f_line)

        mtl_list.append(f"newmtl {self.name}_mtl")
        r, g, b, a = (0, 0, 0, 0)
        try:
            r, g, b, a = self.color.getRgb()
        except AttributeError:
            r, g, b, a = QtGui.QColor(self.color).getRgb()
        mtl_list.append(f"Kd {r/255} {g/255} {b/255} {a/255}")

        obj_list = [obj + "\n" for obj in obj_list]
        mtl_list = [mtl + "\n" for mtl in mtl_list]
        return (obj_list, mtl_list)


class BezierCurve(Wireframe):
    def __init__(
        self, base_points, index, color, normalization_values, window_transformations
    ):
        self.base_points = base_points
        self.coordinates = self.build_bezier_coordinates()
        Wireframe.__init__(
            self,
            self.coordinates,
            index,
            color,
            normalization_values,
            window_transformations,
        )
        self.name = f"Bezier_Curve_{index}"

    def build_bezier_coordinates(self):
        n = 10
        bezier_points = [
            calculate_bezier_points(self.base_points, t)
            for t in np.linspace(0, 1, num=n)
        ]
        return [(x, y) for (x, y) in bezier_points]
