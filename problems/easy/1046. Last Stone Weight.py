from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        if len(stones) == 1:
            return stones[0]

        return stones.pop() - self.lastStoneWeight(stones)


if __name__ == '__main__':
    solution = Solution()
    print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1, 10, 6]))
    assert solution.lastStoneWeight([2, 7, 4, 1, 8, 1, 10, 6]) == 1
    assert solution.lastStoneWeight([1]) == 1
    assert solution.lastStoneWeight([2, 4]) == 2
