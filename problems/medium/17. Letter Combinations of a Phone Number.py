from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letter_in_nums = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            }

        res = []
        need_combine = []
        for digit in digits:
            need_combine.append(letter_in_nums[digit])

        for combination in product(*need_combine):
            res.append(''.join(combination))

        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], f"test 1"
    assert solution.letterCombinations("") == [], f"test 2"
    assert solution.letterCombinations("2") == ["a", "b", "c"], f"test 3"
