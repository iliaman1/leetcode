def titleToNumber(columnTitle: str) -> int:
    res = 0
    for c in columnTitle:
        res = res * 26 + 1 + ord(c) - ord('A')
    return res
