from typing import List
from itertools import combinations


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        for k in range(len(requests), 0, -1):
            for i in combinations(range(len(requests)), k):
                crossing = [0] * n
                for j in i:
                    crossing[requests[j][0]] -= 1
                    crossing[requests[j][1]] += 1

                if not any(crossing):
                    return k

        return 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.maximumRequests(5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]) == 5, 'test 1'
    assert solution.maximumRequests(3, [[0, 0], [1, 2], [2, 1]]) == 3, 'test 2'
    assert solution.maximumRequests(4, [[0, 3], [3, 1], [1, 2], [2, 0]]) == 4, 'test 3'
