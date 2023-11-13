class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        res_vowels = []
        res_string = ''

        for letter in s:
            if letter in vowels:
                res_vowels.append(letter)

        res_vowels.sort(reverse=True)

        for letter in s:
            if letter in vowels:
                res_string += res_vowels.pop()
            else:
                res_string += letter

        return res_string


if __name__ == '__main__':
    solution = Solution()
    assert solution.sortVowels('lEetcOde') == 'lEOtcede', 'test 1 failed'
    assert solution.sortVowels('lYmpH') == 'lYmpH', 'test 2 failed'
