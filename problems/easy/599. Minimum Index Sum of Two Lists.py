from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        basket = {value: index for index, value in enumerate(list1)}
        min_range = 2005
        for index, value in enumerate(list2):
            if value in basket and basket[value] + index < min_range:
                min_range = basket[value] + index
                res.clear()
                res.append(value)
            elif value in basket and basket[value] + index == min_range:
                res.append(value)

        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]) == ["Shogun"], 'test1'
    assert solution.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"]) == ["Shogun"], 'test2'
    assert solution.findRestaurant(
        ["happy", "sad", "good"], ["sad", "happy", "good"]) == ["sad", "happy"], 'test3'
    assert solution.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"]) == ["KFC", "Burger King", "Tapioca Express",
                                                                        "Shogun"], 'test4'
