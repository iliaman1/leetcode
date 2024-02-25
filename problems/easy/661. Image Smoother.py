from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        res = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                current_sum = 0
                current_count = 0
                for x in (i - 1, i, i + 1):
                    for y in (j - 1, j, j + 1):
                        if 0 <= x < m and 0 <= y < n:
                            current_sum += img[x][y]
                            current_count += 1
                res[i][j] = current_sum // current_count

        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.imageSmoother(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    ) == [
               [0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]
           ], 'test 1 failed'
    assert solution.imageSmoother(
        [
            [100, 200, 100],
            [200, 50, 200],
            [100, 200, 100]
        ]
    ) == [
               [137, 141, 137],
               [141, 138, 141],
               [137, 141, 137]
           ], 'test 2 failed'
