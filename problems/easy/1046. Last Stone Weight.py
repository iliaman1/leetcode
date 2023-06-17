from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            stone_max = stones.pop()
            stone_pre_max = stones.pop()
            if stone_max != stone_pre_max:
                stones.append(stone_max - stone_pre_max)
        return stones[0] if stones else 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.lastStoneWeight([2, 7, 4, 1, 8, 1, 10, 6]) == 1
    assert solution.lastStoneWeight([1]) == 1
    assert solution.lastStoneWeight([2, 4]) == 2
    assert solution.lastStoneWeight([2, 2]) == 0
