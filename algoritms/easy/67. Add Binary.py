def strbin_to_int(string: str) -> int:
    res = 0
    for razr9d, number in enumerate(string[::-1]):
        res += int(number) * 2 ** razr9d
    return res


def addBinary(a: str, b: str) -> str:
    return str(bin(strbin_to_int(a) + strbin_to_int(b))).replace('0b', '')


if __name__ == '__main__':
    assert addBinary('11', '1') == "100", 'failed test 1'
    assert addBinary('1010', '1011') == "10101", 'failed test 2'