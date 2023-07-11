from collections import defaultdict


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_freq = j = 0
        basket = defaultdict(int)

        for i in range(len(answerKey)):
            basket[answerKey[i]] += 1

            max_freq = max(max_freq, basket[answerKey[i]])

            if i - j + 1 > max_freq + k:
                basket[answerKey[j]] -= 1
                j += 1

        return len(answerKey) - j


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxConsecutiveAnswers("TTFF", 2) == 4, 'test 1'
    assert solution.maxConsecutiveAnswers("TFFT", 1) == 3, 'test 2'
    assert solution.maxConsecutiveAnswers("TTFTTFTT", 1) == 5, 'test 3'
