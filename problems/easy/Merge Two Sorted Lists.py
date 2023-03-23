class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = temp_head = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                temp_head.next = list1
                list1 = list1.next
            else:
                temp_head.next = list2
                list2 = list2.next
            temp_head = temp_head.next

        if list1:
            temp_head.next = list1
        if list2:
            temp_head.next = list2

        return res.next