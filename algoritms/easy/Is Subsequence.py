def isSubsequence(s: str, t: str) -> bool:
    if s == '':
        return True
    elif len(t) < len(s):
        return False

    index_t = 0
    index_s = 0
    while index_t < len(t):
        if index_s < len(s) and t[index_t] == s[index_s]:
            index_s += 1
        index_t += 1

    if index_s == len(s):
        return True

    return False


if __name__ == '__main__':
    assert isSubsequence("abc", "ahbgdc") == True, 'test 1 failed'
    assert isSubsequence("axc", "ahbgdc") == False, 'test 2 failed'
    assert isSubsequence("b", "abc") == True, 'test 3 failed'
