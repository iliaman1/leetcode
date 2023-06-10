from typing import List
from operator import itemgetter


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        basket = {}
        for index, word in enumerate(words):
            for index2, word2 in enumerate(words):
                if index != index2:
                    if word.endswith(word2) and index2 not in basket:
                        basket[index2] = word2

        for indexes in sorted(basket.keys(), reverse=True):
            del words[indexes]
        return sum([len(i) for i in words]) + len(words) if words else len(basket[0]) + 1


if __name__ == '__main__':
    solution = Solution()
    assert solution.minimumLengthEncoding(["time", "me", "bell"]) == 10
    assert solution.minimumLengthEncoding(["t"]) == 2
    assert solution.minimumLengthEncoding(["me", "time"]) == 5
    assert solution.minimumLengthEncoding(["p", "grah", "qwosp"]) == 11
    assert solution.minimumLengthEncoding(["feipyxx", "e"]) == 10
    assert solution.minimumLengthEncoding(["time", "time", "time", "time"]) == 5
