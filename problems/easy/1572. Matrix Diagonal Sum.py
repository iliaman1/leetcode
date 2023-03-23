def diagonalSum(mat: list[list[int]]) -> int:
    if len(mat) == 1:
        return mat[0][0]
    sum_d = 0
    prim_d_i = 0
    prim_d_j = 0
    sec_d_i = 0
    sec_d_j = len(mat) - 1
    for _ in range(len(mat)):
        if prim_d_i == sec_d_i and prim_d_j == sec_d_j:
            sum_d += mat[prim_d_i][prim_d_j]
            prim_d_i += 1
            prim_d_j += 1
            sec_d_i += 1
            sec_d_j -= 1
            continue
        sum_d += mat[prim_d_i][prim_d_j] + mat[sec_d_i][sec_d_j]
        prim_d_i += 1
        prim_d_j += 1
        sec_d_i += 1
        sec_d_j -= 1

    return sum_d


print(diagonalSum([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]))
