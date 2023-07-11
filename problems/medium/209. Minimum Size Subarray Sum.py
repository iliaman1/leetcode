from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums) < target:
            return 0

        current_sum, l, res = 0, 0, len(nums)

        for r, val in enumerate(nums):
            current_sum += val
            while current_sum >= target:
                current_sum -= nums[l]
                res = min(res, r - l + 1)
                l += 1

        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2, 'test 1'
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1, 'test 2'
    assert solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0, 'test 3'
    assert solution.minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3, 'test 4'
