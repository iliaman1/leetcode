def isMonotonic(nums: list[int]) -> bool:
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)