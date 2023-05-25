'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''


def wordPattern(pattern: str, s: str) -> bool:
    s = s.split()
    basket = {}

    if len(pattern) != len(s):
        return False

    for index, letter in enumerate(pattern):
        if letter not in basket:
            basket[letter] = s[index]
        if basket[letter] != s[index]:
            return False

    if len(set(basket.keys())) != len(set(basket.values())):
        return False

    return True
