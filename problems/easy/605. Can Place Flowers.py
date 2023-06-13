from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fb = [0] + flowerbed + [0]
        for i in range(1, len(fb) - 1):
            if fb[i - 1] == 0 and fb[i] == 0 and fb[i + 1] == 0:
                fb[i] = 1
                n -= 1
        return n <= 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.canPlaceFlowers([0], 1) is True
    assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 1) is True
    assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 2) is False
    assert solution.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2) is True
