'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''


def wordPattern(pattern: str, s: str) -> bool:
    s = [word[0] for word in s.split()]
    if len(pattern) != len(s):
        return False

    return True

wordPattern("abba", "dog cat cat dog")
