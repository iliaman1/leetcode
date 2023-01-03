def mySqrt(x: int) -> int:
    string_x = str(x)
    lst_x = [string_x[i:i + 2] for i in range(0, len(string_x), 2)] if len(string_x) % 2 == 0 else [
        string_x[0]]+[string_x[i:i + 2] for i in range(1, len(string_x), 2)]
    res = []
    remainder = 0
    need_multiplu = None
    tmp_remainder = None
    for i in lst_x:
        i = int(str(remainder)+str(i))
        j = 0
        if not need_multiplu:
            while j * j <= i:
                j += 1
            res.append(j-1)
            need_multiplu = (j-1)*2
            remainder = i - ((j-1) * (j-1))
        else:
            while int(str(need_multiplu) + str(j)) * j <= i:
                tmp_remainder = remainder
                if int(str(need_multiplu) + str(j)) * j <= i:
                    tmp_remainder = i - (int(str(need_multiplu) + str(j)) * j)
                j += 1
            res.append(j-1)
            remainder = tmp_remainder
            need_multiplu = int(''.join([str(i) for i in res])) * 2

    return int(''.join([str(i) for i in res if i < 10]))


if __name__ == '__main__':
    assert mySqrt(2147395599) == 46339, 'failed test 1'
    assert mySqrt(183692038) == 13553, 'failed test 2'
    assert mySqrt(808909662) == 28441, 'failed test 3'
