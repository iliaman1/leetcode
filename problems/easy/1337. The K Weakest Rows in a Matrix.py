from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i[0] for i in sorted([(i, sum(v)) for i, v in enumerate(mat)], key=lambda x: x[1])][:k]


if __name__ == '__main__':
    solution = Solution()
    assert solution.kWeakestRows([
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]], 3) == [2, 0, 3], 'test 1'
    assert solution.kWeakestRows([
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0]], 2) == [0, 2], 'test 2'
