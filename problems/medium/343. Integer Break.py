from functools import cache


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        ans = 1
        while n > 4:
            ans *= 3
            n -= 3

        return ans * n

    def integerBreakDp_d(self, n: int) -> int:
        if n <= 3:
            return n - 1

        dp = [0] * (n + 1)

        # Set base cases
        for i in [1, 2, 3]:
            dp[i] = i

        for num in range(4, n + 1):
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp[num - i])

            dp[num] = ans

        return dp[n]

    def integerBreakDp_u(self, n: int) -> int:
        @cache
        def dp(num):
            if num <= 3:
                return num

            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp(num - i))

            return ans

        if n <= 3:
            return n - 1

        return dp(n)


if __name__ == '__main__':
    solution = Solution()
    assert solution.integerBreak(2) == 1, 'test 1 failed'
    assert solution.integerBreak(10) == 36, 'test 2 failed'
