import json
from typing import List
from point import Point
from functions.cals_square_triangle import square_triangle

class Station:
    def __init__(self, point : Point, code : str):
        self.point = point
        self.code = code

if __name__ == "__main__":
    file = open("data/stations.json")
    data_file = json.load(file)

    data : List[Station] = []

    for elem in data_file:
        if len(elem["xyz"]) == 3 and elem["code"]:
            data += [Station(Point(*elem["xyz"]), elem["code"])]

    print(f"Считано станций: {len(data)}")

    Triangle = [square_triangle(data[0].point, data[1].point, data[2].point)]

    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            for z in range(j + 1, len(data)):
                area = square_triangle(data[i].point, data[j].point, data[z].point)
                if area < Triangle[0]:
                    Triangle = [area, data[i], data[j], data[z]]

    print(f"Min area == {Triangle[0]}")