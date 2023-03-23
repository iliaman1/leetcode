def countOdds(low: int, high: int) -> int:
    return (high - low) // 2 + 1 if (low % 2 == 1 or high % 2 == 1) else (high - low) // 2

# slow solution
# def countOdds(low: int, high: int) -> int:
#     return len([number for number in range(low, high+1) if number % 2 == 1])
