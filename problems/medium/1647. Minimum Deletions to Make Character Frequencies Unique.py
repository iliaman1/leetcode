from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        flag = -100
        lst = list(sorted(counter.values(), reverse=True))
        for i in range(0, len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] == lst[j]:
                    res += 1
                    lst[j] -= 1
                    if lst[j] == 0:
                        lst[j] = flag
                        flag -= 100
        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.minDeletions('aab') == 0, 'test 1'
    assert solution.minDeletions('aaabbbcc') == 2, 'test 2'
    assert solution.minDeletions('ceabaacb') == 2, 'test 3'
    assert solution.minDeletions('bbcebab') == 2, 'test 4'
