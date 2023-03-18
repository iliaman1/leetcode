def isAlienSorted(words: list[str], order: str) -> bool:
    alp = {k: v for k in order, for v in range(len(order))}
    return alp


print(isAlienSorted([], "hlabcdefgijkmnopqrstuvwxyz"))
