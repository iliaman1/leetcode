from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # We collect and sort the value of all n - 1 pairs.
        n = len(weights)
        pair_weights = [0] * (n - 1)
        for i in range(n - 1):
            pair_weights[i] = weights[i] + weights[i + 1]
        pair_weights.sort()

        # Get the difference between the largest k - 1 values and the
        # smallest k - 1 values.
        answer = 0
        for i in range(k - 1):
            answer += pair_weights[n - 2 - i] - pair_weights[i]

        return answer


if __name__ == '__main__':
    solution = Solution()
    assert solution.putMarbles([1, 3, 5, 1], 2) == 4, 'test 1'
    assert solution.putMarbles([1, 3], 2) == 0, 'test 2'
