from collections import defaultdict


class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0
        char_pos = defaultdict(list)
        for i, c in enumerate(s):
            char_pos[c].append(i)
        for a in char_pos.keys():
            for b in char_pos.keys():
                if a == b:
                    continue
                a_idx = b_idx = a_count = b_count = 0
                A, B = len(char_pos[a]), len(char_pos[b])
                while a_idx < A or b_idx < B:
                    if a_idx < A and (b_idx == B or char_pos[a][a_idx] < char_pos[b][b_idx]):
                        a_count += 1
                        a_idx += 1
                    elif b_idx < B:
                        b_count += 1
                        b_idx += 1
                    if b_count < a_count and a_idx < A:
                        a_count = b_count = 0
                    if a_count > 0 < b_count:
                        res = max(res, b_count - a_count)
        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.largestVariance("aababbb") == 3, 'test 1'
    assert solution.largestVariance("abcde") == 0, 'test 2'
