from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        basket = {}
        result = []

        for num in nums:
            if basket.get(num):
                result.append(num)
            else:
                basket[num] = True

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
    assert solution.findDuplicates([1, 1, 2]) == [1]
    assert solution.findDuplicates([1]) == []
