from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in set(nums):
            return len(nums) - 1

        curent_len = 0
        prev_len = 0
        max_len = 0
        l_pointer = 0

        while l_pointer < len(nums):
            if nums[l_pointer] == 1:
                curent_len += 1
            elif nums[l_pointer] == 0:
                prev_len = curent_len
                curent_len = 0

            if max_len < curent_len + prev_len:
                max_len = curent_len + prev_len
            l_pointer += 1

        return max_len


if __name__ == '__main__':
    solution = Solution()
    assert solution.longestSubarray([1, 1, 0, 1]) == 3, 'test 1'
    assert solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5, 'test 2'
    assert solution.longestSubarray([1, 1, 1]) == 2, 'test 3'
