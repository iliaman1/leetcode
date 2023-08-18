import heapq
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)
            res.append(nums[dq[0]])

        return res


if __name__ == '__main__':
    solution = Solution()
    solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    assert solution.maxSlidingWindow([1], 1)
    solution.maxSlidingWindow([1, -1], 1)
    # assert solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    # assert solution.maxSlidingWindow([1], 1) == [1]
    # assert solution.maxSlidingWindow([1, -1], 1) == [1, -1]
