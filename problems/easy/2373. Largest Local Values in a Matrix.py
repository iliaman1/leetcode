class Solution:
    @staticmethod
    def find_max(grid, x, y):
        max_element = 0
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                max_element = max(max_element, grid[i][j])

        return max_element

    @staticmethod
    def largest_local(grid):
        n = len(grid)

        max_local = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                max_local[i][j] = Solution.find_max(grid, i, j)

        return max_local
