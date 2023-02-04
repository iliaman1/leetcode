from collections import Counter
from typing import List


def majorityElement(nums: List[int]) -> int:
    return Counter(nums).most_common()[0][0]


# good solution
# def majorityElement(self, nums: List[int]) -> int:
#     x = len(nums)
#     n = len(nums) // 2
#     while x != 0:
#         if (nums.count(nums[x - 1]) > n):
#             return nums[x - 1]
#         else:
#             x -= 1
