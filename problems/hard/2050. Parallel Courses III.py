from typing import List
from functools import cache
from collections import defaultdict


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        @cache
        def dfs(node):
            if not graph[node]:
                return time[node]

            ans = 0
            for neighbor in graph[node]:
                ans = max(ans, dfs(neighbor))

            return time[node] + ans

        graph = defaultdict(list)
        for (x, y) in relations:
            graph[x - 1].append(y - 1)

        ans = 0
        for node in range(n):
            ans = max(ans, dfs(node))

        return ans


if __name__ == '__main__':
    solution = Solution()
    assert solution.minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]) == 8, 'test 1 failed'
    assert solution.minimumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]) == 12, 'test 2 failed'
