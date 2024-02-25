from typing import List
from collections import Counter


def makeEqual(words: List[str]) -> bool:
    tmp = Counter()
    for word in words:
        tmp += Counter(word)

    for symbol in tmp.values():
        print(symbol)
        if symbol / len(words) < 1:
            return False

    return True


print(makeEqual(['ab', 'a']))
