'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from
magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''
from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    return Counter(ransom_note) <= Counter(magazine)


print(can_construct('a', 'b'))
print(can_construct('aa', 'ab'))
print(can_construct('aa', 'aab'))
