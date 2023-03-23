def subtractProductAndSum(n: int) -> int:
    tmp_lst = list(map(int, str(n)))
    prod = 1
    for elem in tmp_lst:
        prod *= elem
    return prod - sum(tmp_lst)


# math solution
# def subtractProductAndSum(n: int) -> int:
#     sum = 0
#     product = 1
#     while n:
#         sum += n % 10
#         product *= n % 10
#         n //= 10
#
#     return product - sum

