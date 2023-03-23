def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    rows_input = len(mat)
    column_input = len(mat[0])

    if rows_input * column_input != r * c:
        return mat

    lst_mat = [number for lst in mat for number in lst]
    return [lst_mat[i:i + c] for i in range(0, r*c, c)]
