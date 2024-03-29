from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        stack = ["JFK"]
        itinerary = []

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            itinerary.append(stack.pop())

        return itinerary[::-1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC",
                                                                                                        "LHR", "SFO",
                                                                                                        "SJC"]
    assert solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]) == [
        "JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
