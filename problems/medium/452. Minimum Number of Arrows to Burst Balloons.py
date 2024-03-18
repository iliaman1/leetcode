from typing import List


def find_min_arrow_shots(points: List[List[int]]) -> int:
    points.sort(key=lambda x: x[1])

    arrows, end_point = 0, float("-inf")

    for i in points:
        if i[0] > end_point:
            arrows += 1
            end_point = i[1]

    return arrows


find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]])
