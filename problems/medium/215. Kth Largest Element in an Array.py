from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        dec = nums[:k]
        for num in nums:
            if num >= dec[0]:
                del dec[0]
                dec.append(num)

        return dec[0]
