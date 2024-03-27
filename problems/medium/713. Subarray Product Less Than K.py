from typing import List
from math import log
from bisect import bisect


def num_subarray_product_less_than_k(nums: List[int], k: int) -> int:
    if k == 0:
        return 0

    lk = log(k)
    lps = [0]
    for i in nums:
        lps.append(lps[-1] + log(i))

    res = 0
    for i, ln in enumerate(lps):
        j = bisect(lps, ln + lk - 1e-9, i+1)
        res += j - i - 1

    return res

def good_solution(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    n = len(nums)
    prod = 1
    left = 0
    res = 0
    for right in range(n):
        prod *= nums[right]
        while prod >= k:
            prod = prod // nums[left]
            left += 1
        res += right - left + 1
    return res
