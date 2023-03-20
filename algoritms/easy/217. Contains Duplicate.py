from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    # good solution
    def containsDuplicate1(self, nums: List[int]) -> bool:

        numsTracker = {}

        for num in nums:
            if num in numsTracker:
                numsTracker[num] = numsTracker[num] + 1
                if numsTracker[num] > 1:
                    return True
            else:
                numsTracker[num] = 1

        return False
