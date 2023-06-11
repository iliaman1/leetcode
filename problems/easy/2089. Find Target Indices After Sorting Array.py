from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, num in enumerate(sorted(nums)) if num == target]


if __name__ == '__main__':
    solution = Solution()
    assert solution.targetIndices([1, 2, 5, 2, 3], 2) == [1, 2]
    assert solution.targetIndices([1, 2, 5, 2, 3], 3) == [3]
    assert solution.targetIndices([1, 2, 5, 2, 3], 5) == [4]
