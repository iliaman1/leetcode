def removeDuplicates(nums: list[(int, str)]) -> int:
    if not nums:
        return 0

    if len(nums) == 1:
        return 1

    count_unic = 0
    current_index = 0
    while current_index < len(nums):
        if current_index < len(nums) - 1 and type(nums[current_index + 1]) == int \
                and nums[current_index] == nums[current_index + 1]:
            nums.pop(current_index + 1)
            nums.append('_')
        else:
            if nums[current_index] != '_':
                count_unic += 1
            current_index += 1

    return count_unic
