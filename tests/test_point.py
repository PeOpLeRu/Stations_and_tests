import pytest
from point import Point, PointError

@pytest.fixture
def points():
    return Point(0, 0, 0), Point(0, 5, 3)

class TestPoint:
    def test_creation(self):
        Point(1, 2, 3)
        Point(1, 2.2, 3)
        Point(1.5, 1)

        with pytest.raises(PointError):
            Point(1.5, 1, "5")

    def test_additional(self, points):
        p1, p2 = points
        assert p1 + p2 == p2

    def test_substract(self, points):
        p1, p2 = points
        assert p1 - p2 == -p2

    def test_distance_to(self, points):
        p1, p2 = points
        assert p1.distance_to(p2) == pytest.approx(5.8, 0.1)

    @pytest.mark.parametrize(
        "p1, p2, distance",
        [(Point(0, 0, 0), Point(0, 10, 0), 10), 
        (Point(0, 0, 0), Point(10, 0, 0), 10), 
        (Point(0, 0, 0), Point(1, 1, 1), 1.73), 
        ])
    def test_distances_all_exis(self, p1, p2, distance):
        assert p1.distance_to(p2) == pytest.approx(distance, 0.1)

    def test_to_json(self):
        js = '{"x" : 0, "y" : 0.09, "z" : 99}'
        assert Point.from_json(js) == Point(0, 0.09, 99)

    def test_center(self, points):
        p1, p2 = points
        assert p1.is_center()
        assert not p2.is_center()

    def test_eq_with_other_type(self, points):
        p1, p2 = points
        assert p1 == [0, 0, 0]
        assert p2 == (0, 5, 3)

def test_creation():
        Point(1, 2, 3)
        Point(1, 2.2, 3)
        Point(1.5, 1)

        with pytest.raises(PointError):
            Point(1.5, 1, "5")
        
test_creation()