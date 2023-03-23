def maximumWealth(accounts: list[list[int]]) -> int:
    return sum(sorted(accounts, key=lambda x: sum(x), reverse=True)[0])
