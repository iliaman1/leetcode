from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        b = {}
        for i in nums:
            if i in b:
                b[i] += 1
            else:
                b[i] = 1
        n = 0
        c_m = 0
        for i, c in b.items():
            if c > c_m:
                n = c
                c_m = c
            elif c == c_m:
                n += c
        return n
