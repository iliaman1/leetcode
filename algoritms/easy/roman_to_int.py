import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        res = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in roman:
                res += roman[s[i:i + 2]]
                i += 2
            else:
                res += roman[s[i]]
                i += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_roman_to_int(self):
        self.assertEqual(self.solution.romanToInt('III'), 3)
        self.assertEqual(self.solution.romanToInt('LVIII'), 58)
        self.assertEqual(self.solution.romanToInt('MCMXCIV'), 1994)

test = TestSolution()
test.setUp()
test.test_roman_to_int()
unittest.main()