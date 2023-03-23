def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    res = []
    for i in nums1:
        right_max = -1
        for element in nums2[nums2.index(i):]:
            if element > i:
                right_max = element
                break
        res.append(right_max)

    return res
