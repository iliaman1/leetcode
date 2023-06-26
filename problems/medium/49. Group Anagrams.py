from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        basket = {}
        for word in strs:
            tmp = ''.join(sorted(word))
            if tmp in basket:
                basket[tmp].append(word)
            else:
                basket[tmp] = [word]
        return list(basket.values())


if __name__ == '__main__':
    solution = Solution()
    assert solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]
    assert solution.groupAnagrams([""]) == [[""]]
    assert solution.groupAnagrams(["a"]) == [["a"]]
