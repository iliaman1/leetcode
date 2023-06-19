from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        tmp = 0
        max_distance = 0
        for i in gain:
            tmp += i
            if tmp > max_distance:
                max_distance = tmp

        return max_distance


if __name__ == '__main__':
    soluton = Solution()
    assert soluton.largestAltitude([-5, 1, 5, 0, -7]) == 1
    assert soluton.largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0
