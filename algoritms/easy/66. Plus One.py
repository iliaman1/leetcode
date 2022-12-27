def plusOne(digits: list[int]) -> list[int]:
    res = []
    for index, element in digits[::-1]:
        if index == len(digits) - 1 and element == 9:
            res.append(0)
            res.append(1)
        elif element == 9:
            res.append(0)




