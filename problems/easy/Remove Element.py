def removeElement(nums: list[(int, str)], val: int) -> int:
    while val in nums:
        nums.remove(val)
    print(nums)

    return len(nums)
