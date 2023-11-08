class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx - fx == 0 and sy - fy == 0 and t == 1:
            return False
        return t >= max(abs(sx - fx), abs(sy - fy))


if __name__ == '__main__':
    solution = Solution()
    assert solution.isReachableAtTime(2, 4, 7, 7, 6) is True, 'test 1 failed'
    assert solution.isReachableAtTime(3, 1, 7, 3, 3) is False, 'test 2 failed'
    assert solution.isReachableAtTime(1, 2, 1, 2, 1) is False, 'test 3 failed'
    assert solution.isReachableAtTime(1, 1, 1, 1, 3) is True, 'test 4 failed'
