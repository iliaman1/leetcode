def move_zeroes(nums: list[int]) -> None:
    for _ in range(nums.count(0)):
        nums.append(nums.pop(nums.index(0)))


def move_zeroes1(nums: list[int]) -> None:
    pointer_z = 0
    pointer_n = 0
    for _ in range(len(nums)):
        if nums[pointer_z] == 0 and nums[pointer_n] != 0:
            nums[pointer_z], nums[pointer_n] = nums[pointer_n], nums[pointer_z]
        if nums[pointer_z] != 0:
            pointer_z += 1
        pointer_n += 1
