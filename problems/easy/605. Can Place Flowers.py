from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pointer = 0
        count_max_flowers = 0
        while pointer < len(flowerbed)-1:
            if flowerbed[pointer] == 0:





if __name__ == '__main__':
    solution = Solution()
    assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 1) is True
    assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 2) is False
