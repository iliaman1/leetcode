def searchInsert(nums: list[int], target: int) -> int:
    if nums[0] > target:
        return 0

    if nums[-1] < target:
        return len(nums)

    for i in range(len(nums) - 1):
        if nums[i] < target and nums[i + 1] >= target:
            return i+1


print(searchInsert([1,3,5,6], 5))
