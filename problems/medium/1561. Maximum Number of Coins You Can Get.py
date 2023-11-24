from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0

        for i in range(len(piles) // 3, len(piles), 2):
            ans += piles[i]

        return ans


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxCoins([2, 4, 1, 2, 7, 8]) == 9, 'test 1 failed'
    assert solution.maxCoins([2, 4, 5]) == 4, 'test 2 failed'
    assert solution.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]) == 18, 'test 2 failed'
