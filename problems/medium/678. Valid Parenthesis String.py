class Solution:
    def check_valid_string(self, s: str) -> bool:
        open_brackets = []
        asterisks = []

        for i, ch in enumerate(s):
            if ch == "(":
                open_brackets.append(i)
            elif ch == "*":
                asterisks.append(i)
            else:
                if open_brackets:
                    open_brackets.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False

        while open_brackets and asterisks:
            if open_brackets.pop() > asterisks.pop():
                return False

        return not open_brackets


if __name__ == '__main__':
    solution = Solution()
    assert solution.check_valid_string("(*))") is True, 'test 1'
    assert solution.check_valid_string("(((((()*)(*)*))())())(()())())))((**)))))(()())()") is False, 'test 2'
