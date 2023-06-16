from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        basket = {}

        for letter in word:
            if letter not in basket:
                basket[letter] = 1
            else:
                basket[letter] += 1

        
