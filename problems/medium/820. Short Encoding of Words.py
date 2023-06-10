from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        def encode(words: List[str]) -> str:
            res = ''
            index = 0
            while index < len(words):
                if index + 1 < len(words) and (
                        words[index].endswith(words[index + 1]) or words[index + 1].endswith(words[index])):
                    res += words[index] + '#' if words[index].endswith(words[index + 1]) else words[index + 1] + '#'
                    index += 1
                else:
                    res += words[index] + '#'
                index += 1
            return res

        return len(encode(words))


if __name__ == '__main__':
    solution = Solution()
    assert solution.minimumLengthEncoding(["time", "me", "bell"]) == 10
    assert solution.minimumLengthEncoding(["t"]) == 2
    assert solution.minimumLengthEncoding(["me", "time"]) == 5
