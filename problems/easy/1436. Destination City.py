from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        basket = {}

        for a, b in paths:
            basket[a] = b
            if b not in basket:
                basket[b] = None

        for i in basket:
            if not basket[i]:
                return i
