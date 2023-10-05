from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [i for i in Counter(nums) if Counter(nums)[i] > len(nums) / 3]


if __name__ == '__main__':
    solution = Solution()
    assert solution.majorityElement([3, 2, 3]) == [3], 'test 1 failed'
    assert solution.majorityElement([1]) == [1], 'test 2 failed'
    assert solution.majorityElement([1, 2]) == [1, 2], 'test 3 failed'
