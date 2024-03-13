import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        m = [i for i in range(1, n + 1)]
        pref = 0
        post = sum(m)
        for i in m:
            pref += i
            if pref == post:
                return i
            post -= i
        return -1


class MathSolution:
    def pivotInteger(self, n: int) -> int:
        x = math.sqrt(n * (n + 1) / 2)
        converted = int(x)
        return converted if converted == x else -1
