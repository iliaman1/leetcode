from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def common_chars(words: List[str]) -> List[str]:
        n = len(words)
        result = []
        common_character_counts = Counter(words[0])

        for i in range(1, n):
            current_character_counts = Counter(words[i])

            for letter in common_character_counts.keys():
                common_character_counts[letter] = min(
                    common_character_counts[letter],
                    current_character_counts[letter],
                )

        for letter, count in common_character_counts.items():
            for _ in range(count):
                result.append(letter)

        return result


class GoodSolution:
    @staticmethod
    def common_chars(words: List[str]) -> List[str]:
        if len(words) == 1:
            return [words[0]]

        result = []
        chars = set(words[0])

        for char in chars:
            frequency = min([word.count(char) for word in words])
            result += frequency * [char]

        return result
