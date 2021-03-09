import numpy as np
import pytest
from numpy.testing import assert_array_equal, assert_allclose
from app.math_functions import (
    build_translation_matrix,
    build_scaling_matrix,
    build_rotation_matrix,
    build_reflection_matrix,
    normalize_point,
    cohen_sutherland,
)
from app.config import (
    X_MAX_TRANSLATED,
    X_MIN_TRANSLATED,
    Y_MAX_TRANSLATED,
    Y_MIN_TRANSLATED,
    MAX_NORMALIZED_VALUE,
    MIN_NORMALIZED_VALUE,
)


def test_translation_matrix():
    matrix = build_translation_matrix(30, 30)
    expected_matrix = np.array([[1, 0, 0], [0, 1, 0], [30, 30, 1]])
    assert_array_equal(matrix, expected_matrix)


def test_scaling_matrix():
    matrix = build_scaling_matrix(30, 30)
    expected_matrix = np.array([[30, 0, 0], [0, 30, 0], [0, 0, 1]])
    assert_array_equal(matrix, expected_matrix)


def test_rotation_matrix():
    matrix = build_rotation_matrix(30)
    expected_matrix = np.array(
        [[0.86602529158, -0.5, 0], [0.5, 0.86602529158, 0], [0, 0, 1]]
    )
    assert_allclose(matrix, expected_matrix, rtol=1e-5, atol=0)


def test_reflection_matrix_over_x():
    matrix = build_reflection_matrix("x")
    expected_matrix = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
    assert_array_equal(matrix, expected_matrix)


def test_reflection_matrix_over_y():
    matrix = build_reflection_matrix("y")
    expected_matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert_array_equal(matrix, expected_matrix)


def test_reflection_matrix_over_origin():
    matrix = build_reflection_matrix("origin")
    expected_matrix = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
    assert_array_equal(matrix, expected_matrix)


@pytest.mark.skip(reason="no way of currently testing this")
def test_point_normalization_zeros():
    point = (0, 0)
    expected_result = (0, 0)
    normalized = normalize_point(point)
    assert normalized == expected_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_point_normalization_max():
    point = (X_MAX_TRANSLATED, Y_MAX_TRANSLATED)
    expected_result = (1, 1)
    normalized = normalize_point(point)
    assert normalized == expected_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_point_normalization_min():
    point = (X_MIN_TRANSLATED, Y_MIN_TRANSLATED)
    expected_result = (-1, -1)
    normalized = normalize_point(point)
    assert normalized == expected_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_point_normalization_over_boundaries():
    point = (X_MAX_TRANSLATED * 1000, Y_MAX_TRANSLATED * -1000)
    expected_result = (1, -1)
    normalized = normalize_point(point)
    assert normalized == expected_result


def test_cohen_sutherland_both_out():
    is_visible, _, _ = cohen_sutherland((-1.2, -1.2), (1.2, -1.2))
    expected_result = False
    assert is_visible == expected_result


def test_cohen_sutherland_both_in():
    is_visible, _, _ = cohen_sutherland((-0.2, -0.2), (1, -1))
    expected_result = True
    assert is_visible == expected_result


def test_cohen_sutherland_left_out_right_in():
    is_visible, (x0, y0), (x1, y1) = cohen_sutherland((-1.2, -1), (1, -1))
    expected_result_visibility = True
    assert is_visible == expected_result_visibility
    assert (x0, y0) == (-1, -1)
    assert (x1, y1) == (1, -1)


def test_cohen_sutherland_right_out_left_in():
    is_visible, (x0, y0), (x1, y1) = cohen_sutherland((0, 0), (1.2, -1.2))
    expected_result_visibility = True
    assert is_visible == expected_result_visibility
    assert (x0, y0) == (0, 0)
    assert (x1, y1) == (1, -1)


def test_cohen_sutherland_top_out_left_out():
    is_visible, (x0, y0), (x1, y1) = cohen_sutherland((0, 1.2), (1.2, 0.8))
    expected_result_visibility = True
    assert is_visible == expected_result_visibility
    assert (x0, y0) == (0.6, 1)
    assert (x1, y1) == (1, 0.8666666666666667)
