from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = set()
        for element in nums:
            if element in res:
                res.remove(element)
            else:
                res.add(element)

        return list(res)[0]