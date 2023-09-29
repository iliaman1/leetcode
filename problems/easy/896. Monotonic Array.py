from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        currVal = nums[0]
        desc = False
        incr = False
        for i in nums:
            if i < currVal:
                desc = True
            if i > currVal:
                incr = True
            if incr and desc:
                return False
            currVal = i
        return True

        # 1 line
        # return nums == sorted(nums) or nums == sorted(nums, reverse=True)


if __name__ == '__main__':
    solution = Solution()
    assert solution.isMonotonic([1, 2, 2, 3]) is True, 'test 1 failed'
    assert solution.isMonotonic([6, 5, 4, 4]) is True, 'test 2 failed'
    assert solution.isMonotonic([1, 3, 2]) is False, 'test 3 failed'
