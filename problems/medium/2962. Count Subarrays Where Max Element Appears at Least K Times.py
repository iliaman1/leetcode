from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi = -9999
        basket = {}

        for i in nums:
            if i > maxi:
                maxi = i
            if i in basket:
                basket[i] += 1
            else:
                basket[i] = 1

        if basket[maxi] < k:
            return 0

        res = max_elements_in_window = start = 0

        for end in range(len(nums)):
            if nums[end] == maxi:
                max_elements_in_window += 1

            while max_elements_in_window == k:
                if nums[start] == maxi:
                    max_elements_in_window -= 1
                start += 1

            res += start

        return res
