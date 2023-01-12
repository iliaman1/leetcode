from typing import List
# from functools import reduce


def singleNumber(nums: List[int]) -> int:
    for element in nums:
        tmp_lst = nums[:]
        tmp_lst.remove(element)
        if element not in tmp_lst:
            return element


#top rait solution
# def singleNumber(nums: List[int]) -> int:
#     return reduce(lambda total, el: total ^ el, nums)
