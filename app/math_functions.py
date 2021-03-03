import numpy as np

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
    )


def y_viewport_transform(
    y_window, y_window_min, y_window_max, y_viewport_min, y_viewport_max
):
    y_window_min = -1
    y_window_max = 1
    return (1 - ((y_window - y_window_min) / (y_window_max - y_window_min))) * (
        y_viewport_max - y_viewport_min
    )


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


def normalize_function():
    return lambda a, b, min_v, max_v, value: a + (
        (value - min_v) * (b - a) / (max_v - min_v)
    )


def desnormalize_function():
    return (
        lambda a, b, min_v, max_v, value: ((value - a) * (max_v - min_v) / (b - a))
        + min_v
    )


def normalize_point(point, normalization_values):
    x, y = point
    normalize_function
    x_normalized = np.clip(
        normalize_function()(
            MIN_NORMALIZED_VALUE,
            MAX_NORMALIZED_VALUE,
            normalization_values.x_min,
            normalization_values.x_max,
            x,
        ),
        MIN_NORMALIZED_VALUE,
        MAX_NORMALIZED_VALUE,
    )
    y_normalized = np.clip(
        normalize_function()(
            MIN_NORMALIZED_VALUE,
            MAX_NORMALIZED_VALUE,
            normalization_values.y_min,
            normalization_values.y_max,
            y,
        ),
        MIN_NORMALIZED_VALUE,
        MAX_NORMALIZED_VALUE,
    )
    return (x_normalized, y_normalized)


def desnormalize_point(point):
    x_normalized, y_normalized = point

    x = desnormalize_function()(
        MIN_NORMALIZED_VALUE,
        MAX_NORMALIZED_VALUE,
        X_MIN_TRANSLATED,
        X_MAX_TRANSLATED,
        x_normalized,
    )
    y = desnormalize_function()(
        MIN_NORMALIZED_VALUE,
        MAX_NORMALIZED_VALUE,
        Y_MIN_TRANSLATED,
        Y_MAX_TRANSLATED,
        y_normalized,
    )

    return (x, y)

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
