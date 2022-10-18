import pytest
from point import Point
from functions.cals_square_triangle import square_triangle

def test_area():
    assert square_triangle(Point(0, 0, 0), Point(1, 1, 1), Point(2, 2, 2)) == 0
    assert square_triangle(Point(300, 100, 200), Point(1, 150, 1), Point(2, 222, 2)) == pytest.approx(12964, 0.1)