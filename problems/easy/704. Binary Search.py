from typing import List
from math import floor


# не бинарный, а линейный(но проходит)
# def search(nums: List[int], target: int) -> int:
#     for index, element in enumerate(nums):
#         if element == target:
#             return index
#
#     return -1


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    return -1


print(search([5,6,7], 6))
