from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        length = len(obstacleGrid)
        width = len(obstacleGrid[0])
        if length == 1 or width == 1:
            for i in obstacleGrid:
                for j in i:
                    if j == 1:
                        return 0
            return 1

        dp = [[0] * width for _ in range(length)]

        for i in range(width):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break

        for i in range(length):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for i in range(1, length):
            for j in range(1, width):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[length - 1][width - 1]


if __name__ == '__main__':
    solution = Solution()
    solution.uniquePathsWithObstacles([[0, 1, 0], [0, 0, 0], [1, 0, 0]])
    assert solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2, 'test 1'
    assert solution.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1, 'test 2'
    assert solution.uniquePathsWithObstacles([[0, 0]]) == 1, 'test 3'
    assert solution.uniquePathsWithObstacles([[1]]) == 0, 'test 4'
    assert solution.uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]]) == 0, 'test 5'
