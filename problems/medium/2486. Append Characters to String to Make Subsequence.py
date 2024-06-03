class Solution:
    @staticmethod
    def append_characters(s: str, t: str) -> int:
        first, second = 0, 0
        res = len(t)
        n = len(t)

        while first < len(s):
            if second < n and s[first] == t[second]:
                res -= 1
                second += 1

            first += 1

        return res
