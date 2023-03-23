from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        current = head
        last_right = None
        while current:
            if head.next and head.val == head.next.val:
                tmp = head.val
                while head and head.val == tmp:
                    head = head.next
                current = head
                last_right = current
            elif current.next and current.val == current.next.val:
                tmp = current.val
                while current and current.val == tmp:
                    current = current.next
                last_right.next = current
            else:
                last_right = current
                current = current.next

        return head
