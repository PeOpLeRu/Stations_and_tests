import json
import math
from typing import Union

class PointError(Exception):
    ...

class Point:

    def __init__(self, x : Union[int, float] = 0.0, y : Union[int, float] = 0.0, z : Union[int, float] = 0.0) -> None:
        if ((not isinstance(x, int) and not isinstance(x, float)) or
            (not isinstance(y, int) and not isinstance(y, float)) or
            (not isinstance(z, int) and not isinstance(z, float))):
            raise PointError("x, y, z should be integer or float type")
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other : object) -> bool:
        if not isinstance(other, Point):
            if hasattr(other, "__iter__"):
                return self == Point(*other)
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __neg__(self) -> "Point":
        return Point(-self.x, -self.y, -self.z)

    def distance_to(self, other : "Point") -> float:
        return math.sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2) + ((other.z - self.z) ** 2))

    def to_json(self) -> str:
        return json.dumps({"x" : self.x, "y" : self.y, "z" : self.z})
    
    def __str__(self) -> str:
        return f"({self.__class__.__name__}: {self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return f"({self.__class__.__name__}: {self.x}, {self.y}, {self.z})"

    def is_center(self) -> bool:
        return self == Point(0, 0, 0)

    @classmethod
    def from_json(cls: type, s: str) -> "Point":
        js = json.loads(s)
        return cls(float(js["x"]), float(js["y"]), float(js["z"]))