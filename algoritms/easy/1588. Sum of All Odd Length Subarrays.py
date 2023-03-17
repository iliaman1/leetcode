def sumOddLengthSubarrays(arr: list[int]) -> int:
    res, n = 0, len(arr)
    for i, el in enumerate(arr):
        res += ((n - i) * (i + 1) + 1) // 2 * el

    return res
