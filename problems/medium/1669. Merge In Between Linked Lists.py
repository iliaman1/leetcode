class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_in_between(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    s = s_e = e_e = 1
    e = 0
    tmp = head = list1
    while e <= b:
        if s == a:
            s_e = tmp
        elif e == b:
            e_e = tmp.next
        tmp = tmp.next
        s += 1
        e += 1

    s_e.next = list2

    tmp = list2
    while tmp.next:
        tmp = tmp.next

    tmp.next = e_e

    return head
