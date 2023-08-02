from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


if __name__ == '__main__':
    solution = Solution()
    assert solution.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1], f"test 1"
    assert solution.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1], f"test 2"
