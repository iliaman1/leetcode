from heapq import heappop, heappush
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1: List[int], p2: List[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        visited = [False] * n
        heap_dict = {0: 0}
        min_heap = [(0, 0)]

        mst_weight = 0

        while min_heap:
            w, u = heappop(min_heap)

            if visited[u] or heap_dict.get(u, float('inf')) < w:
                continue

            visited[u] = True
            mst_weight += w

            for v in range(n):
                if not visited[v]:
                    new_distance = manhattan_distance(points[u], points[v])

                    if new_distance < heap_dict.get(v, float('inf')):
                        heap_dict[v] = new_distance
                        heappush(min_heap, (new_distance, v))

        return mst_weight


if __name__ == '__main__':
    solution = Solution()
    assert solution.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert solution.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18
