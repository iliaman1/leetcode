from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]

        result = []
        start = last = nums.index(target)
        result.append(start)

        while last + 1 < len(nums) and nums[last + 1] == target:
            last += 1

        result.append(last)

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4], 'test 1 failed'
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1], 'test 2 failed'
    assert solution.searchRange([], 0) == [-1, -1], 'test 3 failed'
    assert solution.searchRange([1], 1) == [0, 0], 'test 4 failed'
