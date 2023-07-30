from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extra = sum(batteries[:-n])
        live = batteries[-n:]
        for i in range(n - 1):
            if extra // (i + 1) < live[i + 1] - live[i]:
                return live[i] + extra // (i + 1)

            extra -= (i + 1) * (live[i + 1] - live[i])

        return live[-1] + extra // n


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxRunTime(2, [3, 3, 3]) == 4
    assert solution.maxRunTime(2, [1, 1, 1, 1]) == 2
