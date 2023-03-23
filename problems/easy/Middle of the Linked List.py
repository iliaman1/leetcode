class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp_head = head
        counter = 0
        while temp_head:
            counter += 1
            temp_head = temp_head.next

        res_counter = counter // 2
        counter = 0
        while counter < res_counter:
            head = head.next
            counter += 1

        return head
