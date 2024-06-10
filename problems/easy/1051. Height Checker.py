from typing import List


class Solution:
    @staticmethod
    def height_checker(heights: List[int]) -> int:
        right_heights = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != right_heights[i]:
                res += 1

        return res
