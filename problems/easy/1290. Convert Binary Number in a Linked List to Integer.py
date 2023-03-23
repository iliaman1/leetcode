class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def get_decimal_value(self, head: ListNode) -> int:
        res = '0b'
        while head:
            res += str(head.val)
            head = head.next
        return int(res, 2)
