import heapq
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        sorted_people = sorted(people)
        dic = {}
        heap = []

        i = 0
        for person in sorted_people:
            while i < len(flowers) and flowers[i][0] <= person:
                heapq.heappush(heap, flowers[i][1])
                i += 1

            while heap and heap[0] < person:
                heapq.heappop(heap)

            dic[person] = len(heap)

        return [dic[x] for x in people]


if __name__ == '__main__':
    solution = Solution()
    assert solution.fullBloomFlowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]) == [1, 2, 2, 2], 'test 1 failed'
    assert solution.fullBloomFlowers([[1, 10], [3, 3]], [3, 3, 2]) == [2, 2, 1], 'test 2 failed'
