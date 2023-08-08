from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n + 1)]


class Solution2:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp


if __name__ == '__main__':
    solution = Solution()
    assert solution.countBits(2) == [0, 1, 1], f"test 1"
    assert solution.countBits(5) == [0, 1, 1, 2, 1, 2], f"test 2"
