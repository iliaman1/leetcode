from collections import Counter


class Solution:
    def custom_sort_string(self, order: str, s: str) -> str:
        cnt = Counter(s)
        s_o = set(order)
        res = ''
        for c in order:
            if c in cnt:
                res += c * cnt[c]
        for c in s:
            if c not in s_o:
                res += c
        return res
