from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    count_zeros = 0
    product = 1
    n = len(nums)
    for i in nums:
        if i == 0:
            count_zeros += 1
            if count_zeros >= 2:
                return [0] * n
            continue
        product *= i

    if count_zeros != 0:
        return [0 if i != 0 else product for i in nums]

    return [product // i for i in nums]
