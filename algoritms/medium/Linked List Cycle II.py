'''список ссылок на объекты и каунтер'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        res_list = []
        while head != None or head not in res_list:
            if head in res_list:
                return head

            res_list.append(head)
            if head == None:
                break
            head = head.next

        return None
