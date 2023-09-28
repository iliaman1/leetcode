from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pointer = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1
        return nums


if __name__ == '__main__':
    solution = Solution()
    assert solution.sortArrayByParity([3, 1, 2, 4]) == [2, 4, 3, 1], 'test 1 failed'
    assert solution.sortArrayByParity([0]) == [0], 'test 2 failed'
