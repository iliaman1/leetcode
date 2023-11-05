from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        count = 0
        winner = arr[0]

        for i in range(1, len(arr)):
            if arr[i] > winner:
                winner = arr[i]
                count = 1
            else:
                count += 1

            if count == k:
                return winner

        return winner


if __name__ == '__main__':
    solution = Solution()
    assert solution.getWinner([2, 1, 3, 5, 4, 6, 7], 2) == 5, 'test 1 failed'
    assert solution.getWinner([3, 2, 1], 10) == 3, 'test 2 failed'
