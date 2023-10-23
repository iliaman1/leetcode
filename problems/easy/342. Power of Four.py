class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        tmp = 1
        while tmp <= n:
            if tmp == n:
                return True

            tmp *= 4

        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.isPowerOfFour(16) is True, 'test 1 failed'
    assert solution.isPowerOfFour(5) is False, 'test 2 failed'
    assert solution.isPowerOfFour(1) is True, 'test 3 failed'
