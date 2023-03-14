from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = pointer2 = head
        while pointer2:
            pointer2 = pointer2.next.next
            pointer1 = pointer1.next

        return pointer1
