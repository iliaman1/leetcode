class Solution:
    @staticmethod
    def find_max_k(nums: list[int]) -> int:
        ans = -1
        seen = set()

        for num in nums:
            abs_num = abs(num)
            if abs_num > ans and -num in seen:
                ans = abs_num
            seen.add(num)

        return ans
