from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2


if __name__ == '__main__':
    solution = Solution()
    assert solution.singleNumber([2, 2, 3, 2]) == 3, 'test 1'
    assert solution.singleNumber([0, 1, 0, 1, 0, 1, 99]) == 99, 'test 2'
