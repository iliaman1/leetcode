from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair = nums[0] + nums[-1]
        l_pointer = 0
        r_pointer = len(nums) - 1
        for _ in range(len(nums) // 2):
            if max_pair < nums[l_pointer] + nums[r_pointer]:
                max_pair = nums[l_pointer] + nums[r_pointer]

            l_pointer += 1
            r_pointer -= 1

        return max_pair


if __name__ == '__main__':
    solution = Solution()
    assert solution.minPairSum([3, 5, 2, 3]) == 7, 'test 1 failed'
    assert solution.minPairSum([3, 5, 4, 2, 4, 6]) == 8, 'test 2 failed'
