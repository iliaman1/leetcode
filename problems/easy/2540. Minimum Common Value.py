from typing import List


def get_сommon_pointer(nums1: List[int], nums2: List[int]) -> int:
    l = 0
    r = 0
    while l < len(nums1) and r < len(nums2):
        if nums1[l] == nums2[r]:
            return nums1[l]
        elif nums1[l] > nums2[r]:
            r += 1
        else:
            l += 1

    return -1


def get_сommon_set(nums1: List[int], nums2: List[int]) -> int:
    return -1 if len(n := set(nums1).intersection(set(nums2))) == 0 else min(n)
