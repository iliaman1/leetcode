from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []

        for i in range(1, n + 1):
            curr_str = ''
            if i % 3 == 0:
                curr_str += 'Fizz'
            if i % 5 == 0:
                curr_str += 'Buzz'
            if curr_str == '':
                curr_str = f'{i}'

            res.append(curr_str)

        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.fizzBuzz(3) == ["1", "2", "Fizz"], 'test 1 failed'
    assert solution.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"], 'test 2 failed'
    assert solution.fizzBuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"], \
        'test 3 failed'
