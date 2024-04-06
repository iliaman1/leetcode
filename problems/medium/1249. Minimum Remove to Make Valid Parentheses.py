from typing import List


class Solution:
    def min_remove_to_make_valid(self, s: str) -> str:
        stack: List[int] = []
        result: List[str] = []
        for c in s:
            if c == '(':
                stack.append(len(result))
                result.append(c)
            elif c == ')':
                if stack:
                    stack.pop()
                    result.append(c)
            else:
                result.append(c)

        for i in stack:
            result[i] = ''

        return ''.join(result)
