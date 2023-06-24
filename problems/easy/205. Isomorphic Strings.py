class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        basket = {}
        if len(s) != len(t):
            return False

        for pointer in range(len(s)):
            if s[pointer] not in basket:
                basket[s[pointer]] = t[pointer]
            elif basket[s[pointer]] != t[pointer]:
                return False

        if len(set(basket.keys())) != len(set(basket.values())):
            return False

        return True


if __name__ == '__main__':
    solution = Solution()
    assert solution.isIsomorphic('egg', 'add') is True, 'test 1 failed'
    assert solution.isIsomorphic("foo", "bar") is False, 'test 2 failed'
    assert solution.isIsomorphic("paper", "title") is True, 'test 3 failed'
    assert solution.isIsomorphic("bbbaaaba", "aaabbbba") is False, 'test 4 failed'
    assert solution.isIsomorphic("abcdefghijklmnopqrstuvwxyzva",
                                 "abcdefghijklmnopqrstuvwxyzck") is False, 'failed test 5'
    assert solution.isIsomorphic("badc", "baba") is False, 'failed test 5'
