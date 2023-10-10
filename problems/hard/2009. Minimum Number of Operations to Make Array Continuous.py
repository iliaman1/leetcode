from typing import List
from bisect import bisect_right


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))

        for i in range(len(new_nums)):
            left = new_nums[i]
            right = left + n - 1
            j = bisect_right(new_nums, right)
            count = j - i
            ans = min(ans, n - count)

        return ans


if __name__ == '__main__':
    solution = Solution()
    assert solution.minOperations([4, 2, 5, 3]) == 0, 'test 1 failed'
    assert solution.minOperations([1, 2, 3, 5, 6]) == 1, 'test 2 failed'
    assert solution.minOperations([1, 10, 100, 1000]) == 3, 'test 3 failed'
