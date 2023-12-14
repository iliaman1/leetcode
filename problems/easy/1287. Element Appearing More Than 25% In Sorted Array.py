from collections import defaultdict
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr) // 4
        counter = defaultdict(int)
        for i in arr:
            counter[i] += 1

            if counter[i] > n:
                return i


if __name__ == '__main__':
    solution = Solution()
    assert solution.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6, 'test 1 failed'
    assert solution.findSpecialInteger([1, 1]) == 1, 'test 2 failed'
