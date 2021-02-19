import pytest
import numpy as np
import simple_math

x1 = np.linspace(0, 1, 10)
x2 = np.linspace(3, 10, 10)

@pytest.mark.parametrize("a, b, expected",
    [(1, 1, 2), (5, 7, 12), (3, 4, 7)])
def test_simple_add(a, b, expected):
    assert simple_math.simple_add(a, b) == expected

@pytest.mark.parametrize("a, b, expected",
    [(1, 1, 0), (5, 7, -2), (3, 4, -1)])
def test_simple_sub(a, b, expected):
    assert simple_math.simple_sub(a, b) == expected

@pytest.mark.parametrize("a, b, expected",
    [(1, 1, 1), (5, 7, 35), (3, 4, 12)])
def test_simple_sub(a, b, expected):
    assert simple_math.simple_mult(a, b) == expected

@pytest.mark.parametrize("a, b, expected",
    [(1, 1, 1), (35, 7, 5), (12, 4, 3)])
def test_simple_div(a, b, expected):
    assert simple_math.simple_div(a, b) == expected

@pytest.mark.parametrize("x, a0, a1, expected",
    [(x1, 2, 1, np.ones(len(x1))*2 + x1), (x2, 0, 4, x2)])
def test_poly_first(x, a0, a1, expected):
    assert np.all(simple_math.poly_first(x, a0, a1)) == np.all(expected)

@pytest.mark.parametrize("x, a0, a1, a2, expected",
    [(x1, 2, 1, 3, np.ones(len(x1)) * 2 + x1 + 3 * x1**2),
    (x2, 0, 4, 5, x2 + 5 * x2**2)])
def test_poly_second(x, a0, a1, a2, expected):
    assert np.all(simple_math.poly_second(x, a0, a1, a2)) == np.all(expected)
