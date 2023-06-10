from typing import List
from operator import itemgetter


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        def encode(words: List[str]) -> str:
            res = ''
            index = 0
            words.sort(key=lambda x: len(x), reverse=True)
            while index < len(words):
                if words[index] + '#' not in res:
                    res += words[index] + '#'
                index += 1
            return res

        return len(encode(words))


if __name__ == '__main__':
    solution = Solution()
    assert solution.minimumLengthEncoding(["time", "me", "bell"]) == 10
    assert solution.minimumLengthEncoding(["t"]) == 2
    assert solution.minimumLengthEncoding(["me", "time"]) == 5
    assert solution.minimumLengthEncoding(["p", "grah", "qwosp"]) == 11
