from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        return money if prices[0] + prices[1] > money else money - (prices[0] + prices[1])


if __name__ == '__main__':
    solution = Solution()
    assert solution.buyChoco([1, 2, 2], 3) == 0, 'test 1'
    assert solution.buyChoco([3, 2, 3], 3) == 3, 'test 2'
