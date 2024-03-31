from typing import List


class Solution:
    def count_subarrays(self, nums: List[int], min_k: int, max_k: int) -> int:
        res = 0
        bad_idx = left_idx = right_idx = -1

        for i, num in enumerate(nums):
            if not min_k <= num <= max_k:
                bad_idx = i

            if num == min_k:
                left_idx = i

            if num == max_k:
                right_idx = i

            res += max(0, min(left_idx, right_idx) - bad_idx)

        return res
