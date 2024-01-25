from utils import fact, roots, integrate
import pytest


def test_fact():
    with pytest.raises(ValueError):
        fact(-1)
        fact("this_is_a_string")
    assert fact(3) == 6
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(5) == 5*4*3*2


def test_roots():
    assert roots(1, 0, 0) == (0)
    assert roots(0, 0, 1) == ()
    assert roots(0, 1, 0) == (0)
    assert roots(1, -2, 1) == (1)
    assert roots(1, 1, -6) == (2, -3) or roots(1, 1, -6) == (-3, 2)


def test_integrate():
    with pytest.raises(ValueError):
        integrate("x", 1, 0)
    assert integrate("x", 0, 1) == 0.5
