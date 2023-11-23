from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            window = sorted(nums[l[i]:r[i] + 1])
            d = window[1] - window[0]
            flag = True
            for j in range(1, len(window)):
                if window[j - 1] + d != window[j]:
                    flag = False
                    break
            res.append(flag)

        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.checkArithmeticSubarrays([4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5]) == [True, False,
                                                                                           True], 'test 1 failed'
    assert solution.checkArithmeticSubarrays([-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], [0, 1, 6, 4, 8, 7],
                                             [4, 4, 9, 7, 9, 10]) == [False, True, False, False, True,
                                                                      True], 'test 2 failed'
