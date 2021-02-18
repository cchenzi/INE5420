from numpy.testing import assert_allclose
from app.wireframe import Wireframe
from app.math_functions import (
    build_translation_matrix,
    build_scaling_matrix,
    build_rotation_matrix,
    build_reflection_matrix,
)


def setup_class(points):
    return Wireframe(points, 0, "foo")


def test_point_translation_A():
    w = setup_class([(1, 3)])
    t = build_translation_matrix(-3, 2)
    w.transformations.append(t)
    w.apply_transformations_to_points()
    expected_points = [(-2, 5)]
    assert w.transformed_coordinates == expected_points


def test_point_translation_B():
    w = setup_class([(-2, 5)])
    t = build_translation_matrix(3, -2)
    w.transformations.append(t)
    w.apply_transformations_to_points()
    expected_points = [(1, 3)]
    assert w.transformed_coordinates == expected_points


def test_point_scaling_C():
    w = setup_class([(4, 5)])
    s = build_scaling_matrix(0.5, 0.5)
    w.transformations.append(s)
    w.apply_transformations_to_points()
    expected_points = [(2, 2.5)]
    assert w.transformed_coordinates == expected_points


def test_point_scaling_D():
    w = setup_class([(2, 2.5)])
    s = build_scaling_matrix(2, 2)
    w.transformations.append(s)
    w.apply_transformations_to_points()
    expected_points = [(4, 5)]
    assert w.transformed_coordinates == expected_points


def test_point_rotation_E():
    w = setup_class([(2, 2.5)])
    r = build_rotation_matrix(30)
    w.transformations.append(r)
    w.apply_transformations_to_points()
    expected_points = [(2.98, 1.16)]
    assert_allclose(w.transformed_coordinates, expected_points, rtol=1e-2, atol=0)


def test_point_rotation_F():
    w = setup_class([(2.98, 1.16)])
    r = build_rotation_matrix(-30)
    w.transformations.append(r)
    w.apply_transformations_to_points()
    expected_points = [(2, 2.5)]
    assert_allclose(w.transformed_coordinates, expected_points, rtol=1e-2, atol=0)


def test_transformations_compositions_G():
    w = setup_class([(1, 3)])
    t = build_translation_matrix(-3, 2)
    w.transformations.append(t)
    t = build_translation_matrix(3, -2)
    w.transformations.append(t)
    w.apply_transformations_to_points()
    expected_points = [(1, 3)]
    assert w.transformed_coordinates == expected_points


def test_transformations_compositions_H():
    w = setup_class([(4, 5)])
    s = build_scaling_matrix(0.5, 0.5)
    w.transformations.append(s)
    s = build_scaling_matrix(2, 2)
    w.transformations.append(s)
    w.apply_transformations_to_points()
    expected_points = [(4, 5)]
    assert w.transformed_coordinates == expected_points


def test_transformations_compositions_I():
    w = setup_class([(2, 2.5)])
    r = build_rotation_matrix(30)
    w.transformations.append(r)
    r = build_rotation_matrix(-30)
    w.transformations.append(r)
    w.apply_transformations_to_points()
    expected_points = [(2, 2.5)]
    assert_allclose(w.transformed_coordinates, expected_points, rtol=1e-2, atol=0)
