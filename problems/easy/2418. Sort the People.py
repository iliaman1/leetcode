from typing import List
import operator


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return list(name for _, name in sorted(zip(heights, names), reverse=True))


if __name__ == '__main__':
    soluton = Solution()
    assert soluton.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]) == ["Mary", "Emma", "John"]
    assert soluton.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]) == ["Bob", "Alice", "Bob"]
