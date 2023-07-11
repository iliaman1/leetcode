class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        if s == goal:
            temp = set(s)
            return len(temp) < len(goal)

        i = 0
        j = n - 1

        while i < j and s[i] == goal[i]:
            i += 1

        while j >= 0 and s[j] == goal[j]:
            j -= 1

        if i < j:
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            s = ''.join(s_list)

        return s == goal


if __name__ == '__main__':
    solution = Solution()
    assert solution.buddyStrings("ab", "ba") is True, 'test 1'
    assert solution.buddyStrings("ab", "ab") is False, 'test 2'
    assert solution.buddyStrings("aa", "aa") is True, 'test 3'
    assert solution.buddyStrings("aba", "baa") is True, 'test 4'
    assert solution.buddyStrings("aaa", "aaa") is True, 'test 5'
    assert solution.buddyStrings("aaaaaaabc", "aaaaaaacb") is True, 'test 6'
    assert solution.buddyStrings("abab", "abab") is True, 'test 7'
    assert solution.buddyStrings("abcd", "abcd") is False, 'test 8'

