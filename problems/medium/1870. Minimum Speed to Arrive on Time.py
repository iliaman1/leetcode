from typing import List
from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) >= hour + 1:
            return -1
        left, right = 1, 10000000
        while left < right:
            mid = (left + right) // 2
            if sum([ceil(i / mid) for i in dist[:-1]]) + (dist[-1] / mid) <= hour:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solution = Solution()
    assert solution.minSpeedOnTime([1, 3, 2], 6) == 1
    assert solution.minSpeedOnTime([1, 3, 2], 2.7) == 3
    assert solution.minSpeedOnTime([1, 3, 2], 1.9) == -1
    assert solution.minSpeedOnTime([4, 2, 3], 2.03) == 100
