class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for char in num:
            while stack and k > 0 and stack[-1] > char:
                stack.pop()
                k -= 1

            stack.append(char)

        stack = stack[:-k] if k > 0 else stack

        return ''.join(stack).lstrip('0') or '0'
