def nearest_valid_point(x: int, y: int, points: list[list[int]]) -> int:
    dist = []
    for index, value in enumerate(points):
        if value[0] == x or value[1] == y:
            dist.append((index, abs(x - value[0]) + abs(y - value[1])))

    if dist:
        return min(dist, key=lambda dis: dis[1])[0]

    return -1


# good solution
def nearest_valid_point1(x: int, y: int, points: list[list[int]]) -> int:
    minn = float('inf')
    index = -1
    for i, v in enumerate(points):
        if v[0] == x or v[1] == y:
            man_dis = abs(x - v[0]) + abs(y - v[1])
            if man_dis < minn:
                minn = man_dis
                index = i

    return index
