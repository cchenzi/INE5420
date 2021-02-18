import numpy as np


def x_viewport_transform(
    x_window, x_window_min, x_window_max, x_viewport_min, x_viewport_max
):
    return ((x_window - x_window_min) / x_window_max - x_window_min) * (
        x_viewport_max - x_viewport_min
    )


def y_viewport_transform(
    y_window, y_window_min, y_window_max, y_viewport_min, y_viewport_max
):
    return (1 - ((y_window - y_window_min) / y_window_max - y_window_min)) * (
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
        [0  0  0]
    """
    matrix = np.zeros((3, 3))
    matrix[0][0] = Sx
    matrix[1][1] = Sy
    return matrix


def build_rotation_matrix(degree):
    """
    Build rotation matrix as:
        [cos(O) -sin(O) 1]
        [sin(O)  cos(O) 1]
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
