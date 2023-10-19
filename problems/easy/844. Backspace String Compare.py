class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        pointer1 = 0
        pointer2 = 0
        lst1 = []
        lst2 = []
        while pointer1 < len(s):
            if s[pointer1] == '#':
                if lst1:
                    lst1.pop()
                pointer1 += 1
                continue
            lst1.append(s[pointer1])
            pointer1 += 1

        while pointer2 < len(t):
            if t[pointer2] == '#':
                if lst2:
                    lst2.pop()
                pointer2 += 1
                continue
            lst2.append(t[pointer2])
            pointer2 += 1

        return lst1 == lst2


if __name__ == '__main__':
    solution = Solution()
    assert solution.backspaceCompare(s="ab#c", t="ad#c") is True, 'test 1 failed'
    assert solution.backspaceCompare(s="ab##", t="c#d#") is True, 'test 2 failed'
    assert solution.backspaceCompare(s="a#c", t="b") is False, 'test 3 failed'
    assert solution.backspaceCompare("a##c", "#a#c") is True, 'test 4 failed'
