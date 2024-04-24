class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        tmp1, tmp2, res = 0, 1, 1
        for i in range(n - 2):
            new_tmp1, new_tmp2 = tmp2, res
            res += tmp1 + tmp2
            tmp1, tmp2 = new_tmp1, new_tmp2

        return res
