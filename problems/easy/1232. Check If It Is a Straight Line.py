def checkStraightLine(coordinates: list[list[int]]) -> bool:
    x1, y1 = coordinates[0][0], coordinates[0][1]
    x2, y2 = coordinates[1][0], coordinates[1][1]
    for x, y in coordinates[2:]:
        if (y - y2) * (x2 - x1) != (x - x2) * (y2 - y1):
            return False

    return True
