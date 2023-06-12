from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        len_row = len(grid[0])
        for i in grid:
            row_counter = 0
            for j in i:
                if j < 0:
                    counter += len_row - row_counter
                    break
                row_counter += 1
        return counter


if __name__ == '__main__':
    solution = Solution()
    assert solution.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8
    assert solution.countNegatives([[3, 2], [1, 0]]) == 0
