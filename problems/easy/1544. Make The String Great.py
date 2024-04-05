class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


class GoodSolution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack:
                if char.lower() == stack[-1].lower() and char != stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return "".join(stack)
