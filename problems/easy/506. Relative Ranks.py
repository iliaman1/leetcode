def find_relative_ranks(score: list[int]) -> list[str]:
    res = []
    places = {k: v for v, k in enumerate(sorted(score, reverse=True))}

    for value in score:
        match places[value]:
            case 0:
                res.append('Gold Medal')
            case 1:
                res.append('Silver Medal')
            case 2:
                res.append('Bronze Medal')
            case _:
                res.append(f'{places[value] + 1}')

    return res


if __name__ == '__main__':
    assert find_relative_ranks([5, 4, 3, 2, 1]) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"], 'test 1'
    assert find_relative_ranks([10, 3, 8, 9, 4]) == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"], 'test 2'
