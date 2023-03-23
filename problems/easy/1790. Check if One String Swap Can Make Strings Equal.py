from collections import Counter

def areAlmostEqual(s1: str, s2: str) -> bool:
    if Counter(s1) == Counter(s2):
        count_diff = 0
        for index in range(len(s1)):
            if s1[index] != s2[index]:
                count_diff += 1

        if count_diff < 3:
            return True

    return False
