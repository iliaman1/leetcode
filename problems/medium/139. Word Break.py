from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                # Handle out of bounds case
                if i < len(word) - 1:
                    continue

                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1:i + 1] == word:
                        dp[i] = True
                        break

        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.wordBreak("leetcode", ["leet", "code"]) is True, f"test 1"
    assert solution.wordBreak("applepenapple", ["apple", "pen"]) is True, f"test 2"
    assert solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False, f"test 3"
