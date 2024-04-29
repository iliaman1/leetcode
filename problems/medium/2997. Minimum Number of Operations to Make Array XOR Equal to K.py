class Solution:
    @staticmethod
    def min_operations(nums: list[int], k: int) -> int:
        final_xor = 0
        for n in nums:
            final_xor = final_xor ^ n

        return bin(final_xor ^ k).count('1')
