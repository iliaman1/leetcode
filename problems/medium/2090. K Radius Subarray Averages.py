from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)

        for i in range(k, len(nums)-k):
            res[i] = sum(nums[i-k:i+k+1])//(k+k+1)

        return res



if __name__ == '__main__':
    solution = Solution()
    assert solution.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3) == [-1, -1, -1, 5, 4, 4, -1, -1, -1]
    assert solution.getAverages([100000], 0) == [100000]
    assert solution.getAverages([8], 100000) == [-1]
