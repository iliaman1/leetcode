from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = sorted([dist[i] / speed[i] for i in range(len(dist))])
        res = 0

        for index in range(len(dist)):
            if time[index] <= index:
                break

            res += 1

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.eliminateMaximum([1, 3, 4], [1, 1, 1]))
    print(solution.eliminateMaximum([1, 1, 2, 3], [1, 1, 1, 1]))
    print(solution.eliminateMaximum([3, 2, 4], [5, 3, 2]))
    print(solution.eliminateMaximum([4, 2, 3], [2, 1, 1]))
