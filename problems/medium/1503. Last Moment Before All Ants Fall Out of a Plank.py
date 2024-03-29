from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left) if left else 0, n - min(right) if right else 0)


if __name__ == '__main__':
    solution = Solution()
    assert solution.getLastMoment(4, [4, 3], [0, 1]) == 4, 'test 1 failed'
    assert solution.getLastMoment(7, [], [0, 1, 2, 3, 4, 5, 6, 7]) == 7, 'test 2 failed'
    assert solution.getLastMoment(4, [0, 1, 2, 3, 4, 5, 6, 7], []) == 7, 'test 3 failed'
