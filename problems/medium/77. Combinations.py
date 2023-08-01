from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()
        output = []
        backtrack()
        return output



if __name__ == '__main__':
    solution = Solution()
    assert solution.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4],
                                      [3, 4]], f"test 1 = {solution.combine(4, 2)}"
    assert solution.combine(1, 1) == [[1]], f"test 2 = {solution.combine(1, 1)}"
