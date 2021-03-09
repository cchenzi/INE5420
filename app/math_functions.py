import numpy as np
from functools import reduce
from app.utils import get_reflection_indexes, transformations_codes
from app.config import (
    X_MAX_TRANSLATED,
    X_MIN_TRANSLATED,
    Y_MAX_TRANSLATED,
    Y_MIN_TRANSLATED,
    MAX_NORMALIZED_VALUE,
    MIN_NORMALIZED_VALUE,
)


def x_viewport_transform(
    x_window, x_window_min, x_window_max, x_viewport_min, x_viewport_max
):
    x_window_min = -1
    x_window_max = 1
    return ((x_window - x_window_min) / (x_window_max - x_window_min)) * (
        x_viewport_max - x_viewport_min
    ) + 20


def y_viewport_transform(
    y_window, y_window_min, y_window_max, y_viewport_min, y_viewport_max
):
    y_window_min = -1
    y_window_max = 1
    return (1 - ((y_window - y_window_min) / (y_window_max - y_window_min))) * (
        y_viewport_max - y_viewport_min
    ) + 20


def build_translation_matrix(Dx, Dy):
    """
    Build translation matrix as:
        [1   0  0]
        [0   1  0]
        [Dx  Dy 1]
    """
    matrix = np.identity(3)
    matrix[2][0] = Dx
    matrix[2][1] = Dy
    return matrix


def build_scaling_matrix(Sx, Sy):
    """
    Build scaling matrix as:
        [Sx 0  0]
        [0  Sy 0]
        [0  0  1]
    """
    matrix = np.identity(3)
    matrix[0][0] = Sx
    matrix[1][1] = Sy
    return matrix


def build_rotation_matrix(degree):
    """
    Build rotation matrix as:
        [cos(O) -sin(O) 0]
        [sin(O)  cos(O) 0]
        [0       0      1]
    """
    matrix = np.identity(3)
    cos = np.cos(np.deg2rad(degree))
    sin = np.sin(np.deg2rad(degree))
    matrix[0][0] = cos
    matrix[1][1] = cos
    matrix[0][1] = -sin
    matrix[1][0] = sin
    return matrix


def build_reflection_matrix(over):
    """
    Build reflection matrix as:
        [1  0  0]
        [0  1  0]
        [0  0  1],
    where over determine where to
    apply the reflection: x, y or origin.
    """
    matrix = np.identity(3)
    for index in get_reflection_indexes(over):
        matrix[index] = -1
    return matrix


transformations_functions_dict = {
    "rf": build_reflection_matrix,
    "rt": build_rotation_matrix,
    "r_rt": build_rotation_matrix,
    "sc": build_scaling_matrix,
    "r_sc": build_scaling_matrix,
    "tr": build_translation_matrix,
}


def build_homogeneous_coordinates(coordinates):
    ones = np.ones((len(coordinates), 1))
    return np.hstack((coordinates, ones))


def calculate_object_center(coordinates):
    return tuple(np.array(coordinates).mean(axis=0))


def multiply_coordinates_by_transformations(coordinates, transformations):

    return np.dot(coordinates, transformations)


def normalize_point(point, height, width):
    x, y = point
    return (x / height, y / width)


def build_window_normalizations(
    window_x_shift, window_y_shift, window_width, window_height, window_angle
):
    translation_matrix = transformations_functions_dict["tr"](
        window_x_shift, window_y_shift
    )
    rotation_matrix = transformations_functions_dict["rt"](window_angle)

    scaling_matrix = transformations_functions_dict["sc"](
        2 / window_width, 2 / window_height
    )

    composition = reduce(np.dot, [translation_matrix, rotation_matrix, scaling_matrix])

    return composition


def transform_coordinates(x, y, window_coordinates, viewport_coordinates):
    xvp = x_viewport_transform(
        x,
        window_coordinates.x_min,
        window_coordinates.x_max,
        viewport_coordinates.x_min,
        viewport_coordinates.x_max,
    )
    yvp = y_viewport_transform(
        y,
        window_coordinates.y_min,
        window_coordinates.y_max,
        viewport_coordinates.y_min,
        viewport_coordinates.y_max,
    )
    return (xvp, yvp)


def get_angle(x, x1, x2):
    return (x - x1) / (x2 - x1)


def get_cohen_sutherland_point_code(
    value, min_value, max_value, lower_code, upper_code
):
    if value > max_value:
        return upper_code
    if value < min_value:
        return lower_code
    return 0


def cohen_sutherland(p1, p2):
    top = 8
    bottom = 4
    left = 1
    right = 2

    x_min = -1
    y_min = -1
    x_max = 1
    y_max = 1

    p0_code = 0
    x0, y0 = p1
    p0_code += get_cohen_sutherland_point_code(x0, x_min, x_max, left, right)
    p0_code += get_cohen_sutherland_point_code(y0, y_min, y_max, bottom, top)

    p1_code = 0
    x1, y1 = p2
    p1_code += get_cohen_sutherland_point_code(x1, x_min, x_max, left, right)
    p1_code += get_cohen_sutherland_point_code(y1, y_min, y_max, bottom, top)
    while True:

        print(p0_code, p1_code, p0_code & p1_code, p0_code | p1_code)
        # Both out from window
        if p0_code & p1_code != 0:
            return (False, (x0, y0), (x1, y1))
        # Both in
        if p0_code | p1_code == 0:
            return (True, (x0, y0), (x1, y1))

        x = 0
        y = 0

        outside_code = max(p0_code, p1_code)
        if outside_code & left == left:
            y = y0 + (y1 - y0) * (x_min - x0) / (x1 - x0)
            x = x_min
        if outside_code & right == right:
            y = y0 + (y1 - y0) * (x_max - x0) / (x1 - x0)
            x = x_max

        if outside_code & top == top:
            x = x0 + (x1 - x0) * (y_max - y0) / (y1 - y0)
            y = y_max

        if outside_code & bottom == bottom:
            x = x0 + (x1 - x0) * (y_min - y0) / (y1 - y0)
            y = y_min

        if outside_code == p0_code:
            x0 = x
            y0 = y
            p0_code = 0
            p0_code += get_cohen_sutherland_point_code(x0, x_min, x_max, left, right)
            p0_code += get_cohen_sutherland_point_code(y0, y_min, y_max, bottom, top)
        else:
            x1 = x
            y1 = y
            p1_code = 0
            p1_code += get_cohen_sutherland_point_code(x1, x_min, x_max, left, right)
            p1_code += get_cohen_sutherland_point_code(y1, y_min, y_max, bottom, top)

    return (False, None, None)


def clip(wireframe, method=None):
    # Apply point clipping
    if wireframe.number_points == 1:
        coord_aux = np.array(wireframe.transformed_coordinates[0])
        if np.any((coord_aux < -1) | (coord_aux > 1)):
            print(f"Coords {coord_aux} not visible!")
            is_visible = False
            return is_visible, None
        else:
            print(f"Coords {coord_aux} visible!")
            is_visible = True
            return is_visible, [coord_aux]
    if wireframe.number_points == 2:
        p1 = wireframe.transformed_coordinates[0]
        p2 = wireframe.transformed_coordinates[1]
        is_visible, new_p1, new_p2 = cohen_sutherland(p1, p2)
        return is_visible, [new_p1, new_p2]
