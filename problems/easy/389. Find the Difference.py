from collections import Counter


def findTheDifference(s: str, t: str) -> str:
    s = Counter(s)
    t = Counter(t)
    res = t - s

    return ''.join(res.keys())


# good solution
def findTheDifference1(s: str, t: str) -> str:
    for i in set(t):
        if s.count(i) != t.count(i):
            return i
