from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]
        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left] = max(nums[left] - dp[left + 1],
                               nums[right] - dp[left])
        return dp[0] >= 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.PredictTheWinner([1, 5, 2]) is False, 'test 1'
    assert solution.PredictTheWinner([1, 5, 233, 7]) is True, 'test 2'
