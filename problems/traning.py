from typing import Optional


def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    if not s:
        return

    temp = s.pop()
    reverseString(s)
    s.insert(0, temp)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        me_useles = head.next.next
        temp = head
        head = head.next
        temp.next = head.next
        head.next = temp
        temp.next = self.swapPairs(me_useles)

        return head
