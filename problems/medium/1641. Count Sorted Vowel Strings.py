from math import factorial


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return factorial(4 + n) // (factorial(4) * factorial(n))


if __name__ == '__main__':
    solution = Solution()
    assert solution.countVowelStrings(1) == 5
    assert solution.countVowelStrings(2) == 15
    assert solution.countVowelStrings(33) == 66045
