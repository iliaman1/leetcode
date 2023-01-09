from typing import List


def generate(numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        row_0 = [1]
        row_1 = [1, 1]
        res = [row_0] + [row_1] + [[1] + [1] * i for i in range(2, numRows + 1)]

        for i in range(2, len(res)):
            for j in range(1, len(res[i]) - 1):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

    return res
