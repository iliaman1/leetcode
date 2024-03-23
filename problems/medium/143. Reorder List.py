from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tmp = head
        res = []
        while tmp:
            res.append(tmp)
            tmp = tmp.next

        tmp = head
        l, r = 1, len(res) - 1
        while l <= r:
            tmp.next = res[r]
            tmp = res[r]
            tmp.next = res[l]
            tmp = res[l]
            l += 1
            r -= 1
        tmp.next = None
