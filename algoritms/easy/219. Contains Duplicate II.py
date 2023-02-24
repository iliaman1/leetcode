from typing import List


# try 4
# accepted
def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    dup = {}
    for index in range(len(nums)):
        if nums[index] in dup and abs(dup[nums[index]] - index) <= k:
            return True

        dup[nums[index]] = index

    return False

# try 3
# Time Limit Exceeded
# def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
#     dup = {}
#     for elem in set(nums):
#         if nums.count(elem) > 1:
#             dup[elem] = []
#             current_index = nums.index(elem)
#             for _ in range(nums.count(elem)):
#                 dup[elem].append(current_index)
#                 try:
#                     current_index = nums.index(elem, current_index+1)
#                 except:
#                     continue
#
#     for lst in dup.values():
#         for i in range(len(lst)-1):
#             if abs(lst[i] - lst[i+1]) <= k:
#                 return True
#     return False


# try 2
# Time Limit Exceeded
# def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
#     dup = []
#     for elem in set(nums):
#         if nums.count(elem) > 1:
#             dup.append(elem)
#
#     for index, element in enumerate(nums):
#         if element in dup and element in nums[index + 1: index + 1 + k]:
#             return True
#     return False


# try 1
# Time Limit Exceeded
# def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
#     for index, element in enumerate(nums):
#         if element in nums[index+1: index + 1 + k]:
#             return True
#     return False
