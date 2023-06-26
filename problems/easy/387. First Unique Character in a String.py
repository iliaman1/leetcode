from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        basket = defaultdict(int)
        for char in s:
            basket[char] += 1

        for index, char in enumerate(s):
            if basket[char] == 1:
                return index

        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.firstUniqChar("leetcode") == 0
    assert solution.firstUniqChar("loveleetcode") == 2
    assert solution.firstUniqChar("aabb") == -1
