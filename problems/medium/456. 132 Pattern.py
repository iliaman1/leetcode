from typing import List
from bisect import bisect_left


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i - 1], nums[i])

        k = len(nums)
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            k = bisect_left(nums, min_array[j] + 1, k, len(nums))
            if k < len(nums) and nums[k] < nums[j]:
                return True
            k -= 1
            nums[k] = nums[j]
        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.find132pattern([1, 2, 3, 4]) is False, 'test 1 failed'
    assert solution.find132pattern([3, 1, 4, 2]) is True, 'test 2 failed'
    assert solution.find132pattern([-1, 3, 2, 0]) is True, 'test 3 failed'
