from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]


if __name__ == '__main__':
    solution = Solution()
    assert solution.nextGreatestLetter(["c", "f", "j"], "a") == "c"
    assert solution.nextGreatestLetter(["c", "f", "j"], "c") == "f"
    assert solution.nextGreatestLetter(["x", "x", "y", "y"], "z") == "x"
