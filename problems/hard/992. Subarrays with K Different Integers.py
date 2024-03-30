from collections import defaultdict
from typing import List


def subarrays_with_k_distinct(nums: List[int], k: int) -> int:
    distinct_count = defaultdict(int)
    total_count = left = right = curr_count = 0
    while right < len(nums):
        distinct_count[nums[right]] += 1

        if distinct_count[nums[right]] == 1:
            k -= 1

        if k < 0:
            distinct_count[nums[left]] -= 1
            if distinct_count[nums[left]] == 0:
                k += 1
            left += 1
            curr_count = 0

        if k == 0:
            while distinct_count[nums[left]] > 1:
                distinct_count[nums[left]] -= 1
                left += 1
                curr_count += 1

            total_count += curr_count + 1

        right += 1

    return total_count
