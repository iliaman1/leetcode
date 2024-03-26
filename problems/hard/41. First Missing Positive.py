from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        t = (i for i in range(1, len(nums) + 2))
        for i in nums:
            if i < 1:
                continue
            else:
                e = t.__next__()
                if e == i:
                    continue
                else:
                    return e
        return t.__next__()


class GoodSolution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        cntr = set(nums)
        i = 1
        while i in cntr:
            i += 1
        return i
