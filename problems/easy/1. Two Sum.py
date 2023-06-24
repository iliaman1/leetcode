from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        basket = {}
        for index, val in enumerate(nums):
            if val in basket:
                return [basket[val], index]
            else:
                basket[target - val] = index


if __name__ == '__main__':
    solution = Solution()
    assert solution.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert solution.twoSum(nums=[3, 2, 4], target=6) == [1, 2]
    assert solution.twoSum(nums=[3, 3], target=6) == [0, 1]
