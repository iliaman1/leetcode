class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {')': '(', '}': '{', ']': '['}
        open = '({['
        close = ')]}'
        for i in s:
            if i in open:
                stack.append(i)
            if i in close:
                if not stack:
                    return False
                if stack.pop() != my_dict[i]:
                    return False
                else:
                    continue
        if not stack:
            return True
        return False


if __name__ == '__main__':
    tr = Solution()
    assert tr.isValid("()") == True, 'что-то пошло не по плану'
    assert tr.isValid("()[]{}") == True, 'что-то пошло не по плану'
    assert tr.isValid("(]") == False, 'что-то пошло не по плану'
