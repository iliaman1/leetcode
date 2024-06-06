from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def is_n_straight_hand(hand: List[int], group_size: int) -> bool:
        # Step 1: Check if grouping is possible
        if len(hand) % group_size != 0:
            return False

        # Step 2: Count the occurrences of each card
        count = Counter(hand)

        # Step 3: Sort the unique card values
        sorted_keys = sorted(count.keys())

        # Step 4: Form consecutive groups
        for key in sorted_keys:
            if count[key] > 0:  # If this card is still available
                start_count = count[key]
                # Check and form a group starting from `key`
                for i in range(key, key + group_size):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count

        return True
