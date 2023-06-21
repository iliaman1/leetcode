from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dictcoder = {}
        pointer = 0
        for letter in key.replace(' ', ''):
            if letter not in dictcoder:
                dictcoder[letter] = ascii_lowercase[pointer]
                pointer += 1

        res = ''

        for char in message:
            if char in dictcoder:
                res += dictcoder[char]
            else:
                res += ' '

        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.decodeMessage("the quick brown fox jumps over the lazy dog",
                                  "vkbs bs t suepuv") == "this is a secret"
    assert solution.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo",
                                  "zwx hnfx lqantp mnoeius ycgk vcnjrdb") == "the five boxing wizards jump quickly"
