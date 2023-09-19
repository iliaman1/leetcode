from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num)
            if nums[idx] < 0:
                return idx
            nums[idx] = -nums[idx]
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    assert solution.findDuplicate([1, 3, 4, 2, 2]) == 2, 'test 1'
    assert solution.findDuplicate([3, 1, 3, 4, 2]) == 3, 'test 2'
