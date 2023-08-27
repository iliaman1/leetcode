class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            columnNumber -= 1
            ans += chr(columnNumber % 26 + ord('A'))
            columnNumber //= 26

        return ans[::-1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.convertToTitle(1) == 'A', 'test 1'
    assert solution.convertToTitle(28) == 'AB', 'test 2'
    assert solution.convertToTitle(701) == 'ZY', 'test 3'
