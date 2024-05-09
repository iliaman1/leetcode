class Solution:
    @staticmethod
    def maximum_happiness_sum(happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        i = 0
        res = 0

        while k > 0:
            happiness[i] = max(happiness[i] - i, 0)
            res += happiness[i]
            i += 1
            k -= 1

        return res
