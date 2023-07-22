from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        tmp = float('-inf')
        res = 0

        for start, end in intervals:
            if start >= tmp:
                tmp = end
            else:
                res += 1

        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1, 'test 1'
    assert solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2, 'test 2'
    assert solution.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0, 'test 3'
    assert solution.eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2, 'test 4'
