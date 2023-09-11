from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res_dict = {}
        res = []

        for index, elem in enumerate(groupSizes):
            if elem not in res_dict:
                res_dict[elem] = [index]
            else:
                res_dict[elem].append(index)

        for key in res_dict.keys():
            for i in range(0, len(res_dict[key]), key):
                res.append(res_dict[key][i:i + key])


        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.groupThePeople([3, 3, 3, 3, 3, 1, 3]) == [[5], [0, 1, 2], [3, 4, 6]], 'test 1'
    assert solution.groupThePeople([2, 1, 3, 3, 3, 2]) == [[1], [0, 5], [2, 3, 4]], 'test 2'
