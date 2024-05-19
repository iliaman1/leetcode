from typing import List


class Solution:
    @staticmethod
    def maximum_value_sum(nums: List[int], k: int, edges: List[List[int]]) -> int:
        total_sum = 0
        count = 0
        positive_min = float("inf")
        negative_max = float("-inf")

        for node_value in nums:
            node_val_after_operation = node_value ^ k

            total_sum += node_value
            net_change = node_val_after_operation - node_value

            if net_change > 0:
                positive_min = min(positive_min, net_change)
                total_sum += net_change
                count += 1
            else:
                negative_max = max(negative_max, net_change)

        if count % 2 == 0:
            return total_sum
        return max(total_sum - positive_min, total_sum + negative_max)
