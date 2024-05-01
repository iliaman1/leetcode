class Solution:
    @staticmethod
    def reversePrefix(word: str, ch: str) -> str:
        for i, e in enumerate(word):
            if e == ch:
                return word[i::-1] + word[i + 1:]
        return word


if __name__ == '__main__':
    assert Solution.reversePrefix('abcdefd', 'd') == 'dcbaefd', 'test 1'
    assert Solution.reversePrefix('xyxzxe', 'z') == 'zxyxxe', 'test 2'
    assert Solution.reversePrefix('abcd', 'z') == 'abcd', 'test 3'
