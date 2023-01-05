from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    tmp = []
    pointer_nums1 = 0
    pointer_nums2 = 0
    while pointer_nums1 < m and pointer_nums2 < n:
        if nums1[pointer_nums1] <= nums2[pointer_nums2]:
            tmp.append(nums1[pointer_nums1])
            pointer_nums1 += 1
        else:
            tmp.append(nums2[pointer_nums2])
            pointer_nums2 += 1
    if pointer_nums1 < m:
        while pointer_nums1 < m:
            tmp.append(nums1[pointer_nums1])
            pointer_nums1 += 1
    else:
        while pointer_nums2 < n:
            tmp.append(nums2[pointer_nums2])
            pointer_nums2 += 1
    nums1.clear()
    for i in tmp:
        nums1.append(i)

#good solution
# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     nums1[m:] = nums2[0:]
#     nums1.sort()