from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while list1 != None or list2 != None:
            if list1 == None:
                res.append(list2.val)
                list2 = list2.next
            elif list2 == None:
                res.append(list1.val)
                list1 = list1.next
            elif list1.val <= list2.val:
                res.append(list1.val)
                list1 = list1.next
            else:
                res.append(list2.val)
                list2 = list2.next
        return res

if __name__ == '__main__':
    test = Solution()
    assert test.mergeTwoLists([1,2,4],[1,3,4]) == [1,1,2,3,4,4], "равные списки не прошли"
    assert test.mergeTwoLists([], []) == [], "пустые списки не прошли"
    assert test.mergeTwoLists([], [0]) == [0], "один пустой, другой нет не прошло"
