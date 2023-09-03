class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.uniquePaths(3, 7) == 28, 'test 1'
    assert solution.uniquePaths(3, 2) == 3, 'test 2'
