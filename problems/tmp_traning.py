def get_max_bowling_score(lst: list) -> int:
    if not lst:
        return 0

    return max(
        get_max_bowling_score(lst[1:]),
        get_max_bowling_score(lst[1:]) + lst[0],
        get_max_bowling_score(lst[2:]) + lst[0] * lst[1]) if len(lst) >= 2 else max(
        get_max_bowling_score(lst[1:]),
        get_max_bowling_score(lst[1:]) + lst[0]
    )


if __name__ == '__main__':
    assert get_max_bowling_score([-3, 5, 2]) == 10, f"test 1 = {get_max_bowling_score([-3, 5, 2])}"
    assert get_max_bowling_score([-3, -5, -5]) == 25, f"test 2 = {get_max_bowling_score([-3, -5, -5])}"
    assert get_max_bowling_score([-3, -5, -5, -7]) == 50, f"test 3 = {get_max_bowling_score([-3, -5, -5, -7])}"
    assert get_max_bowling_score([-3, -5, -5, -7, -7]) == 74, f"test 4 = {get_max_bowling_score([-3, -5, -5, -7, -7])}"
