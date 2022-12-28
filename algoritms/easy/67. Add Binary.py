def addBinary(a: str, b: str) -> str:
    res_numb_a = 0
    stepen_a = 0
    res_numb_b = 0
    stepen_b = 0
    for digit in a:
        res_numb_a += int(digit) * 2**stepen_a
        stepen_a += 1
    for digit in b:
        res_numb_b += int(digit) * 2**stepen_b
        stepen_b += 1

    return str(bin(int(res_numb_a)+int(res_numb_b))).replace('0b', '')


print(addBinary('1010', '1011'))
