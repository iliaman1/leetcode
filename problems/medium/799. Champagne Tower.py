class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r + 1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r + 1][c] += q
                    A[r + 1][c + 1] += q

        return min(1, A[query_row][query_glass])


if __name__ == '__main__':
    solution = Solution()
    assert solution.champagneTower(1, 1, 1) == 0, 'test 1 failed'
    assert solution.champagneTower(2, 1, 1) == 0.5, 'test 2 failed'
    assert solution.champagneTower(100000009, 33, 17) == 1, 'test 3 failed'