from typing import List


def trap(height: List[int]) -> int:
    left, right, left_max, right_max, res = 0, len(height) - 1, 0, 0, 0

    while left < right:
        current_left, current_right = height[left], height[right]

        if current_left < current_right:
            if current_left >= left_max:
                left_max = current_left
            else:
                res += left_max - current_left
            left += 1
        else:
            if current_right >= right_max:
                right_max = current_right
            else:
                res += right_max - current_right
            right -= 1

    return res
