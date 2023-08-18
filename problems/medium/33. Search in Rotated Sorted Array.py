from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        if nums[0] > nums[-1]:
            left = 0
            right = len(nums) - 1
            while left < right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[right]:
                    left = pivot + 1
                else:
                    right = pivot

            if nums[pivot] < target < nums[pivot + 1]:
                return -1

            left = 0
            right = len(nums) - 1
            if target < nums[right]:
                left = pivot
            else:
                right = pivot - 1

            while left <= right:
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        else:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.search([3, 1], 3) == 0, 'test -2'
    assert solution.search([1, 3], 3) == 1, 'test -1'
    assert solution.search([7, 0, 1, 2, 4, 5, 6], 0) == 1, 'test 0'
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4, 'test 1'
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1, 'test 2'
    assert solution.search([1], 0) == -1, 'test 3'
