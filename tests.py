import pytest
from shapes import *

def test_area_of_rectangle():
    assert area_of_rectangle(5, 10) == 50

    with pytest.raises(ValueError):
        area_of_rectangle(-5, 10)

def test_area_of_circle():
    assert area_of_circle(3) == pytest.approx(28.274333882308138, rel=1e-9)

    with pytest.raises(ValueError):
        area_of_circle(-3)

def test_area_of_triangle():
    assert area_of_triangle(6, 4) == 12

    with pytest.raises(ValueError):
        area_of_triangle(-6, 4)

def test_area_of_zero():
    assert area_of_rectangle(0, 0) == 0
    assert area_of_circle(0) == 0
    assert area_of_triangle(0, 0) == 0