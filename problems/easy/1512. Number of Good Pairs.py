from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        gp = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    gp += 1

        return gp


if __name__ == '__main__':
    solution = Solution()
    assert solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4, 'test 1 failed'
    assert solution.numIdenticalPairs([1, 1, 1, 1]) == 6, 'test 2 failed'
    assert solution.numIdenticalPairs([1, 2, 3]) == 0, 'test 3 failed'
