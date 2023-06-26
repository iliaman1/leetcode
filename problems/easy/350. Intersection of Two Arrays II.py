from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tmp = Counter(nums2)
        res = []
        for i in nums1:
            if i in tmp and tmp[i] > 0:
                tmp[i] -= 1
                res.append(i)
        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]) in ([4, 9], [9, 4])
    assert solution.intersect([1, 2, 2, 1], [2]) == [2]
