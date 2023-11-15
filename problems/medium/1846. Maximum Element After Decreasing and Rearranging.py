from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        current = 1
        for i in range(1, len(arr)):
            if arr[i] > current:
                current += 1
        return current


if __name__ == '__main__':
    solution = Solution()
    assert solution.maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]) == 2, 'test 1 failed'
    assert solution.maximumElementAfterDecrementingAndRearranging([100, 1, 1000]) == 3, 'test 2 failed'
    assert solution.maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5]) == 5, 'test 3 failed'
