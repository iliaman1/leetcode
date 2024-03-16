from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m = {0: -1}
        m_len = c = 0
        for i in range(len(nums)):
            c = c + (1 if nums[i] == 1 else -1)
            if c in m:
                m_len = max(m_len, i - m[c])
            else:
                m[c] = i
        return m_len
