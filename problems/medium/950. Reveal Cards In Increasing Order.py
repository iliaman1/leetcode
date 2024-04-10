from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        queue = deque()

        # Create a queue of indexes
        for i in range(N):
            queue.append(i)

        deck.sort()

        # Put cards at correct index in result
        result = [0] * N
        for card in deck:
            # Reveal Card
            result[queue.popleft()] = card

            # Move next card to bottom
            if queue:
                queue.append(queue.popleft())

        return result


class PointerSolution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        result = [0] * N
        skip = False
        index_in_deck = 0
        index_in_result = 0

        deck.sort()

        while index_in_deck < N:
            # There is an available gap in result
            if result[index_in_result] == 0:

                # Add a card to result
                if not skip:
                    result[index_in_result] = deck[index_in_deck]
                    index_in_deck += 1

                # Toggle skip to alternate between adding and skipping cards
                skip = not skip

            # Progress to the next index of result array
            index_in_result = (index_in_result + 1) % N

        return result
