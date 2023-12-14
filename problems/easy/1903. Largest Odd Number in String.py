class Solution:
    def largestOddNumber(self, num: str) -> str:
        odds = {'1', '3', '5', '7', '9'}
        for i in range(len(num)-1, -1, -1):
            if num[i] in odds:
                return num[:i+1]

        return ''


if __name__ == '__main__':
    solution = Solution()
    assert solution.largestOddNumber('52') == '5', 'test 1 failed'
    assert solution.largestOddNumber('4206') == '', 'test 2 failed'
    assert solution.largestOddNumber('35427') == '35427', 'test 3 failed'
