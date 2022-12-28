def mySqrt(x: int) -> int:
    res = 0
    while res * res <= x:
        if res * res == x:
            return res
        if res + 1 * res + 1 > x:
            return res
        res+=1
    return res


print(mySqrt(4))
# if __name__ == '__main__':
#     assert mySqrt(4) == 2, 'failed test 1'
#     assert mySqrt(8) == 2, 'failed test 2'
