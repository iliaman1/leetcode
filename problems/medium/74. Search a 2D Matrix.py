from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, column = len(matrix), len(matrix[0])

        row_index = -1

        l_r = 0
        while l_r <= rows:
            mid_row = l_r + (rows - l_r) // 2
            if matrix[mid_row][0] > target:
                rows = mid_row - 1
            elif matrix[mid_row][-1] < target:
                l_r = mid_row + 1
            else:
                row_index = mid_row

        if row_index == -1:
            return False

        target_row = matrix[row_index]
        l_c = 0
        while l_c <= column:
            if matrix[row_index][-1] >= target:
                mid = left + (right - left) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                continue

        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ], 3) is True
    assert solution.searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ], 13) is False
