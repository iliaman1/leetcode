def mySqrt(x: int) -> int:
    string_x = str(x)
    lst_x = [int(string_x[i:i + 2]) for i in range(0, len(string_x), 2)] if len(string_x) % 2 == 0 else [
        int(string_x[::-1][i:i + 2]) for i in range(0, len(string_x), 2)][::-1]
    res = []
    ostatok = None
    need_multiplu = None
    prev_res = 0
    tmp_ostatok = None
    for i in lst_x:
        j = 0
        if ostatok:
            i = int(str(ostatok)+str(i))
        if need_multiplu:
            while int(str(need_multiplu)+str(j)) * j <= i:
                tmp_ostatok = ostatok
                if int(str(need_multiplu)+str(j)) * j <= i:
                    prev_res = j
                    tmp_ostatok = i - int(str(need_multiplu)+str(j)) * j
                j += 1
            ostatok = tmp_ostatok
        else:
            while j * j <= i:
                if j * j <= i:
                    prev_res = j
                    ostatok = i - prev_res * prev_res
                j += 1

        res.append(prev_res)
        need_multiplu = prev_res*2
        print(i)
        print(prev_res)
        print(ostatok)
        print(need_multiplu, '\n')

    return int(''.join([res[i] for i in range(len(res)) if res[i] < 10]))


print(mySqrt(101761))
# if __name__ == '__main__':
#     assert mySqrt(4) == 2, 'failed test 1'
#     assert mySqrt(8) == 2, 'failed test 2'
