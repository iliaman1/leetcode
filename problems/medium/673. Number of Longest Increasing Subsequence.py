from typing import List


# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
#         res = 0
#         pointer = 0
#         tmp = nums[0]
#         while pointer < len(nums):
#             if tmp >= nums[pointer]:
#                 res += 1
#             tmp = nums[pointer]
#             pointer += 1
#
#         return res

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_length = max(length)
        result = 0

        for i in range(n):
            if length[i] == max_length:
                result += count[i]

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.findNumberOfLIS([1, 3, 5, 4, 7]) == 2, 'test 1'
    assert solution.findNumberOfLIS([2, 2, 2, 2, 2]) == 5, 'test 2'
    assert solution.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]) == 3, 'test 3'
