from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        dp = [1] * n
        ans = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
            ans = max(ans, dp[i])
        return ans

    def findLongestChain1(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        max_len = 1
        maxNum = pairs[0][1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > maxNum:
                max_len += 1
                maxNum = pairs[i][1]
        return max_len


if __name__ == '__main__':
    solution = Solution()
    assert solution.findLongestChain([[1, 2], [2, 3], [3, 4]]) == 2, 'test 1'
    assert solution.findLongestChain([[1, 2], [7, 8], [4, 5]]) == 3, 'test 2'
