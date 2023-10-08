from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                use = nums1[i] * nums2[j] + dp[i + 1][j + 1]
                dp[i][j] = max(use, dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

    def maxDotProduct_upgraded(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        m = len(nums2) + 1
        prev_dp = [0] * m
        dp = [0] * m

        for i in range(len(nums1) - 1, -1, -1):
            dp = [0] * m
            for j in range(len(nums2) - 1, -1, -1):
                use = nums1[i] * nums2[j] + prev_dp[j + 1]
                dp[j] = max(use, prev_dp[j], dp[j + 1])

            prev_dp = dp

        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxDotProduct([2, 1, -2, 5], [3, 0, -6]) == 18, 'test 1 failed'
    assert solution.maxDotProduct([3, -2], [2, -6, 7]) == 21, 'test 2 failed'
    assert solution.maxDotProduct([-1, -1], [1, 1]) == -1, 'test 3 failed'
