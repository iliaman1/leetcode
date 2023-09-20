from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, n = sum(nums) - x, len(nums)

        if target == 0:
            return n

        max_len = cur_sum = left = 0

        for right, val in enumerate(nums):
            cur_sum += val
            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len else -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.minOperations([1, 1, 4, 2, 3], 5) == 2, 'test 1'
    assert solution.minOperations([5, 6, 7, 8, 9], 4) == -1, 'test 2'
    assert solution.minOperations([3, 2, 20, 1, 1, 3], 10) == 5, 'test 3'
