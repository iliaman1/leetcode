from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) == 1:
            return adjacentPairs[0]

        restored_memories = {}
        counter = 0

        for i in adjacentPairs:
            for j in i:
                if j in restored_memories:
                    restored_memories[j] += 2
                else:
                    restored_memories[j] = counter
                counter += 1
            counter += 5

        print(restored_memories)


if __name__ == '__main__':
    solution = Solution()
    assert solution.restoreArray([[2, 1], [3, 4], [3, 2]]) == [1, 2, 3, 4], 'test 1 failed'
    assert solution.restoreArray([[4, -2], [1, 4], [-3, 1]]) == [-2, 4, 1, -3], 'test 2 failed'
    assert solution.restoreArray([[100000, -100000]]) == [100000, -100000], 'test 3 failed'
