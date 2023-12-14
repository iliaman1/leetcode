from collections import defaultdict
from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid[0]), len(grid)
        row_1, col_1, row_0, col_0 = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    row_0[i] += 1
                    col_0[j] += 1
                else:
                    row_1[i] += 1
                    col_1[j] += 1

        for i in range(n):
            for j in range(m):
                grid[i][j] = row_1[i] + col_1[j] - row_0[i] - col_0[j]

        return grid


if __name__ == '__main__':
    solution = Solution()
    assert solution.onesMinusZeros(
        [
            [0, 1, 1],
            [1, 0, 1],
            [0, 0, 1]
        ]
    ) == [
               [0, 0, 4],
               [0, 0, 4],
               [-2, -2, 2]
           ], 'test 1 failed'
    assert solution.onesMinusZeros(
        [
            [1, 1, 1],
            [1, 1, 1]
        ]
    ) == [
               [5, 5, 5],
               [5, 5, 5]
           ], 'test 2 failed'
