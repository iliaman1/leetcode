from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfairness = float('inf')
        distribution = [0] * k

        def backtrack(i):
            nonlocal min_unfairness, distribution

            if i == len(cookies):
                min_unfairness = min(min_unfairness, max(distribution))
                return

            if min_unfairness <= max(distribution):
                return

            for j in range(k):
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]

        backtrack(0)
        return min_unfairness


if __name__ == '__main__':
    solution = Solution()
    assert solution.distributeCookies([8, 15, 10, 20, 8], 2) == 31, 'test 1'
    assert solution.distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3) == 7, 'test 2'
