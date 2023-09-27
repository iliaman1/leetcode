class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        i = 0

        while length < k:
            if s[i].isdigit():
                length *= int(s[i])
            else:
                length += 1
            i += 1

        for j in range(i - 1, -1, -1):
            char = s[j]
            if char.isdigit():
                length //= int(char)
                k %= length
            else:
                if k == 0 or k == length:
                    return char
                length -= 1


if __name__ == '__main__':
    solution = Solution()
    assert solution.decodeAtIndex('leet2code3', 10) == "o", 'test 1 failed'
    assert solution.decodeAtIndex('ha22', 5) == "h", 'test 2 failed'
    assert solution.decodeAtIndex('a2345678999999999999999', 1) == "a", 'test 3 failed'
