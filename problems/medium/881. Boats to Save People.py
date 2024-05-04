class Solution:
    @staticmethod
    def num_rescue_boats(people: list[int], limit: int) -> int:
        res = 0
        people.sort()
        l, r = 0, len(people) - 1
        while l <= r:
            tmp = people[r]
            r -= 1
            if tmp + people[r] <= limit:
                r -= 1
                res += 1
                continue
            elif tmp + people[l] <= limit:
                l += 1
                res += 1
                continue
            else:
                res += 1
        return res


class SolutionB:
    @staticmethod
    def num_rescue_boats(people: list[int], limit: int) -> int:
        people.sort()
        people.reverse()
        ans, l, r = 0, 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                r -= 1
            l += 1
            ans += 1
        return ans


if __name__ == '__main__':
    assert Solution.num_rescue_boats([1, 2], 3) == 1, 'test 1'
    assert Solution.num_rescue_boats([3, 2, 2, 1], 3) == 3, 'test 2'
    assert Solution.num_rescue_boats([3, 5, 3, 4], 5) == 4, 'test 3'
    assert Solution.num_rescue_boats([3, 2, 3, 2, 2], 6) == 3, 'test 4'
