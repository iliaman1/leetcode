def reverseBits(n: int) -> int:
    n = str(n)[::-1]
    res = 0
    for razr9d, number in enumerate(n[::-1]):
        res += int(number) * 2 ** razr9d
    return res


print(reverseBits(11111111111111111111111111111101))
