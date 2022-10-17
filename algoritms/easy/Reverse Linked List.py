class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        current = head
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev


lst = [1, 2, 3, 4, 5]
true_head = head = ListNode(lst[0])
for i in lst[1:]:
    head.next = ListNode(i)
    head = head.next

test = Solution.reverseList(true_head)
while test.next:
    print(test.val)
    test = test.next
