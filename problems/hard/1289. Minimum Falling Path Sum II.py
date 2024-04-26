from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = grid[0]

        for i in range(1, n):
            left = row.index(min(row))
            right = row.index(min(row[:left] + row[left + 1:]))

            for j in range(n):
                grid[i][j] += row[left] if j != left else row[right]

            row = grid[i]

        return min(row)
