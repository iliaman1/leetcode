from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        most_see = counter.most_common()[0][1]
        if len(s) == 1:
            return s

        if 2 * most_see - len(s) > 1:
            return ''

        s = sorted(s, key=lambda x: (counter.get(x), -ord(x)), reverse=True)
        ans = [0] * len(s)
        pointer = 0
        for i in range(0, len(s), 2):
            ans[i] = s[pointer]
            pointer += 1

        for i in range(1, len(s), 2):
            ans[i] = s[pointer]
            pointer += 1

        return ''.join(ans)


if __name__ == '__main__':
    solution = Solution()
    assert solution.reorganizeString("aab") == 'aba', 'test 1'
    assert solution.reorganizeString("aaab") == '', 'test 2'
    assert solution.reorganizeString("vvvlo") == 'vlvov', 'test 3'
    assert solution.reorganizeString("abbabbaaab") == 'ababababab', 'test 4'
