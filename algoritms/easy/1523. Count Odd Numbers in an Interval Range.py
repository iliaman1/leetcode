def countOdds(low: int, high: int) -> int:

    return len([number for number in range(low, high+1) if number % 2 == 1])