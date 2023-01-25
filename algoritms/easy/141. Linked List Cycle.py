from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list_prev = []
        while head != None:
            if head in list_prev:
                return True
            list_prev.append(head)
            head = head.next
        return False


#good solution
# def hasCycle(self, head):
#     Initialize two node slow and fast point to the hesd node...
#     fastptr = head
#     slowptr = head
#     while fastptr is not None and fastptr.next is not None:
#         Move slow pointer by 1 node and fast at 2 at each step.
#         slowptr = slowptr.next
#         fastptr = fastptr.next.next
#         If both the pointers meet at any point, then the cycle is present and return true...
#         if slowptr == fastptr:
#             return 1
#     return 0