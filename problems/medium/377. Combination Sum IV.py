from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]


if __name__ == '__main__':
    solution = Solution()
    assert solution.combinationSum4([1, 2, 3], 4) == 7, 'test 1'
    assert solution.combinationSum4([9], 3) == 0, 'test 2'
