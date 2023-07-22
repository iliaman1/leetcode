from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = ''
        number2 = ''
        l1_head = l1
        l2_head = l2

        while l1_head:
            number1 += str(l1_head.val)
            l1_head = l1_head.next

        while l2_head:
            number2 += str(l2_head.val)
            l2_head = l2_head.next

        if not number1:
            number1 = 0
        if not number2:
            number2 = 0

        res_number = str(int(number1) + int(number2))
        res_list = ListNode()
        res_list_head = res_list
        counter = 0

        while counter < len(res_number):
            res_list_head.val = int(res_number[counter])
            if counter + 1 < len(res_number):
                res_list_head.next = ListNode()
                res_list_head = res_list_head.next
            counter += 1

        return res_list
