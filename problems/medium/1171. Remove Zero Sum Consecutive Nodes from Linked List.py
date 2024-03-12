from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_zero_sum_sublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sums = {0: front}
        while current:
            prefix_sum += current.val
            prefix_sums[prefix_sum] = current
            current = current.next
        prefix_sum = 0
        current = front
        while current:
            prefix_sum += current.val
            current.next = prefix_sums[prefix_sum].next
            current = current.next
        return front.next
