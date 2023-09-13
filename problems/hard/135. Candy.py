from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


if __name__ == '__main__':
    solution = Solution()
    assert solution.candy([1, 0, 2]) == 5, 'test 1'
    assert solution.candy([1, 2, 2]) == 4, 'test 2'
    assert solution.candy([1, 3, 2, 2, 1]) == 7, 'test 3'
    assert solution.candy([1, 2, 87, 87, 87, 2, 1]) == 13, 'test 4'
    assert solution.candy([1, 6, 10, 8, 7, 3, 2]) == 18, 'test 5'
