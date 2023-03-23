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
        if not head:
            return
        if not head.next:
            return head
        if not head.next.next:
            temp = head
            head = head.next
            head.next = temp
            temp.next = None

        temp = head
        head = head.next
        temp.next = head.next.next
        head.next = temp
        self.swapPairs(head.next)


lst = [1, 2, 3, 4]
head = ListNode(lst[0])
elem1 = ListNode(lst[1])
elem2 = ListNode(lst[2])
elem3 = ListNode(lst[3])
head.next = elem1
elem1.next = elem2
elem2.next = elem3

temp = head
while temp:
    print(temp.val)
    temp = temp.next

temp = head
solv = Solution()
solv.swapPairs(temp)

print(elem3.next.val)
