from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pointer = 0
        while asteroids and pointer + 1 < len(asteroids):
            if asteroids[pointer] < 0 < asteroids[pointer + 1]:
                pointer += 1
                continue
            elif asteroids[pointer] > 0 > asteroids[pointer + 1]:
                if asteroids[pointer] == abs(asteroids[pointer + 1]):
                    del asteroids[pointer + 1]
                    del asteroids[pointer]
                    pointer -= 1
                elif asteroids[pointer] > abs(asteroids[pointer + 1]):
                    del asteroids[pointer + 1]
                elif asteroids[pointer] < abs(asteroids[pointer + 1]):
                    del asteroids[pointer]
                    pointer -= 1
                pointer -= 1
            if pointer < 0:
                pointer = -1
            pointer += 1

        return asteroids


# good runtime solution
# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         stack = []
#
#         for asteroid in asteroids:
#             while stack and asteroid < 0 and stack[-1] > 0:
#                 if abs(asteroid) > stack[-1]:
#                     stack.pop()
#                     continue
#                 elif abs(asteroid) == stack[-1]:
#                     stack.pop()
#                 break
#             else:
#                 stack.append(asteroid)
#
#         return stack

# good memory solution
# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         i=0
#         while i < len(asteroids):
#             if asteroids[i] < 0 and asteroids[i - 1] >= 0 and abs(asteroids[i]) > asteroids[i - 1] and i != 0:
#                 asteroids.pop(i-1)
#                 i -= 1
#             elif asteroids[i] < 0  and abs(asteroids[i]) < asteroids[i - 1] and i != 0:
#                 asteroids.pop(i)
#             elif asteroids[i] < 0  and asteroids[i] + asteroids[i - 1] == 0 and i != 0:
#                 asteroids.pop(i)
#                 asteroids.pop(i-1)
#                 i-=1
#             else:
#                 i +=1
#         return asteroids


if __name__ == '__main__':
    solution = Solution()
    assert solution.asteroidCollision([5, 10, -5]) == [5, 10], 'test 1'
    assert solution.asteroidCollision([8, -8]) == [], 'test 2'
    assert solution.asteroidCollision([10, 2, -5]) == [10], 'test 3'
    assert solution.asteroidCollision([8, 8, -8]) == [8], 'test 4'
    assert solution.asteroidCollision([1, -2, -2, 1]) == [-2, -2, 1], 'test 5'
    assert solution.asteroidCollision([-2, -2, 1, -2]) == [-2, -2, -2], 'test 6'
    assert solution.asteroidCollision([1, 1, -1, -2]) == [-2], 'test 7'
