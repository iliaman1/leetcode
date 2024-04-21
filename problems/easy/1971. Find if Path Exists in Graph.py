import heapq
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def valid_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        distances = {node: float('inf') for node in range(n)}
        distances[source] = 0
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_node == destination:
                return True

            if current_distance > distances[current_node]:
                continue

            for neighbor in graph[current_node]:
                distance = current_distance + 1  # Assuming unweighted graph
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return False
