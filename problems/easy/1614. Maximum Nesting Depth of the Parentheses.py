class Solution:
    @staticmethod
    def max_depth(s: str) -> int:
        res = tmp = 0
        for i in s:
            if i == '(':
                tmp += 1
            elif i == ')':
                tmp -= 1
            if tmp > res:
                res = tmp

        return res
