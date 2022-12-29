def mySqrt(x: int) -> int:
    string_x = str(x)
    lst_x = [int(string_x[i:i + 2]) for i in range(0, len(string_x), 2)] if len(string_x) % 2 == 0 else [
        int(string_x[::-1][i:i + 2]) for i in range(0, len(string_x), 2)][::-1]
    res = []
    ostatok = None
    need_multiplu = None
    prev_res = 0
    for i in lst_x:
        j = 0
        if ostatok:
            i = int(str(ostatok)+str(i))
        if need_multiplu:
            while int(str(prev_res)+str(j)) * 2 <= i:
                if int(str(prev_res)+str(j)) * 2 <= i:
                    prev_res = j
                    ostatok = i - prev_res
                j += 1
        else:
            while j * j <= i:
                if j * j <= i:
                    prev_res = j
                    ostatok = i - prev_res
                j += 1

        res.append(prev_res)
        need_multiplu = prev_res*2

    return res


print(mySqrt(81))
# if __name__ == '__main__':
#     assert mySqrt(4) == 2, 'failed test 1'
#     assert mySqrt(8) == 2, 'failed test 2'
