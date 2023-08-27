class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2:
            return False

        for i in range(1, len(s) // 2 + 1):
            if s[:i] * (len(s) // i) == s:
                return True

        return False


class GoodSolution:
    def goodrepeatedSubstringPattern(self, s: str) -> bool:
        s_fold = "".join((s[1:], s[:-1]))

        return s in s_fold


if __name__ == '__main__':
    solution = Solution()
    assert solution.repeatedSubstringPattern("abab") is True, 'test 1'
    assert solution.repeatedSubstringPattern("aba") is False, 'test 2'
    assert solution.repeatedSubstringPattern("abcabcabcabc") is True, 'test 3'
    assert solution.repeatedSubstringPattern("ab") is False, 'test 4'
