from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left_pointer = 0
        right_pointer = k
        current_window = nums[left_pointer:right_pointer]
        current_max = max(current_window)
        counter = current_window.index(current_max)
        result = []
        while right_pointer <= len(nums):
            if counter == 0:
                current_window = nums[left_pointer:right_pointer]
                counter = current_window.index(current_max)
            if nums[right_pointer] > current_max:
                current_max = nums[right_pointer]
            result.append(current_max)
            left_pointer += 1
            right_pointer += 1
            counter -= 1


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert solution.maxSlidingWindow([1], 1) == [1]
