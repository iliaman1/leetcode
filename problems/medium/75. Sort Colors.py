from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l_pointer = 0
        r_pointer = len(nums) - 1
        current = 0
        while current <= r_pointer:
            if nums[current] == 0:
                nums[current], nums[l_pointer] = nums[l_pointer], nums[current]
                l_pointer += 1

            elif nums[current] == 2:
                nums[current], nums[r_pointer] = nums[r_pointer], nums[current]
                r_pointer -= 1
                current -= 1

            current += 1


sol = Solution()
sol.sortColors([1, 2, 0])
