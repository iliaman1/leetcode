def lengthOfLastWord(s: str) -> int:
    while '  ' in s:
        s = s.replace('  ', ' ')

    return len(s.split()[-1])


if __name__ == '__main__':
    assert lengthOfLastWord("Hello World") == 5, 'test 1 failed'
    assert lengthOfLastWord("   fly me   to   the moon  ") == 4, 'test 2 failed'
    assert lengthOfLastWord("luffy is still joyboy") == 6, 'test 3 failed'


# def lengthOfLastWord(self, s):
#     ls = len(s)
    # slow and fast pointers
    # slow = -1
    # iterate over trailing spaces
    # while slow >= -ls and s[slow] == ' ':
    #     slow-=1
    # fast = slow
    # iterate over last word
    # while fast >= -ls and s[fast] != ' ':
    #     fast-=1
    # return slow - fast