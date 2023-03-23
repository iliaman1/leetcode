def arraySign(nums: list[int]) -> int:
    count_negative = 0
    for number in nums:
        if number == 0:
            return 0
        if number < 0:
            count_negative += 1
    return -1 if count_negative % 2 != 0 else 1
