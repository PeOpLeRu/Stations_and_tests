import math
from point import Point

def square_triangle(p1 : Point, p2 : Point, p3 : Point) -> float:
    return math.sqrt(
                    (((p2.x * p1.y) - (p3.x * p1.y) - (p1.x * p2.y) + (p3.x * p2.y) + (p1.x * p3.y) - (p2.x * p3.y)) ** 2) + 
                    (((p2.x * p1.z) - (p3.x * p1.z) - (p1.x * p2.z) + (p3.x * p2.z) + (p1.x * p3.z) - (p2.x * p3.z)) ** 2) + 
                    (((p2.y * p1.z) - (p3.y * p1.z) - (p1.y * p2.z) + (p3.y * p2.z) + (p1.y * p3.z) - (p2.y * p3.z)) ** 2)
                    ) / 2