from math import ceil


class Solution:
    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)
        dp = {}

        def calculate_dp(i, j):
            return (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][j - 1] +
                    dp[max(0, i - 2)][max(0, j - 2)]
                    + dp[i - 1][max(0, j - 3)]) / 4

        dp[0] = {0: 0.5}
        for k in range(1, m + 1):
            dp[0][k] = 1
            dp[k] = {0: 0}
            for j in range(1, k + 1):
                dp[j][k] = calculate_dp(j, k)
                dp[k][j] = calculate_dp(k, j)
            if dp[k][k] > 1 - 1e-5:
                return 1
        return dp[m][m]

# best
# class Solution:
#     def soupServings(self, n: int) -> float:
#         # return p(a empty) & p(a&b empty)
#         if n >= 4500:
#             return 1.0
#
#         @lru_cache(None)
#         def r(a, b):
#             if a <= 0 and b <= 0:
#                 return .5
#             elif a <= 0:
#                 return 1.0
#             elif b <= 0:
#                 return 0
#             else:
#                 return .25 * (r(a - 100, b) + r(a - 50, b - 50) + r(a - 25, b - 75) + r(a - 75, b - 25))
#
#         return r(n, n)
