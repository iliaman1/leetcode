from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = None
        less_head = None
        equal_bigger = None
        equal_bigger_head = None

        while head:
            if head.val < x and not less_head:
                less_head = less = head
            elif head.val < x:
                less.next = head
                less = less.next
            elif head.val >= x and not equal_bigger_head:
                equal_bigger_head = equal_bigger = head
            else:
                equal_bigger.next = head
                equal_bigger = equal_bigger.next

            head = head.next

        if less_head:
            less.next = equal_bigger_head
        if equal_bigger_head:
            equal_bigger.next = None

        return less_head or equal_bigger_head
