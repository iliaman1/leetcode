def convert_chars(text: str) -> str:
    dict_text = {}
    symbol_text = 0
    for symbol in text:
        if symbol not in dict_text:
            dict_text[symbol] = chr(symbol_text)
            symbol_text += 1
        else:
            continue

    res_string = ''
    for i in text:
        res_string += dict_text[i]

    return res_string


def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    if convert_chars(s) == convert_chars(t):
        return True

    return False


if __name__ == '__main__':
    assert isIsomorphic('egg', 'add') == True, 'test 1 failed'
    assert isIsomorphic("foo", "bar") == False, 'test 2 failed'
    assert isIsomorphic("paper", "title") == True, 'test 3 failed'
    assert isIsomorphic("bbbaaaba", "aaabbbba") == False, 'test 4 failed'
    assert isIsomorphic("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck") == False, 'failed test 5'
