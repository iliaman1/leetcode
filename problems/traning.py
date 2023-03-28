from typing import Optional, List
from math import factorial
from functools import reduce
from operator import mul


def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    if not s:
        return

    temp = s.pop()
    reverseString(s)
    s.insert(0, temp)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    me_useles = head.next.next
    temp = head
    head = head.next
    temp.next = head.next
    head.next = temp
    temp.next = self.swapPairs(me_useles)

    return head


def reverseList1(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    prev = None
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    return prev


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    new_head = reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root.val == val:
        return root

    if root.left:
        return searchBST(root.left, val)

    if root.right:
        return searchBST(root.right, val)


# не будем пересчитывать факториал, через хелпер  а = числитель, б = знаменатель, ц = текущий шаг
def getRow(rowIndex: int) -> List[int]:
    result = [1]
    current_factorial = 1
    current_numerator = rowIndex
    for i in range(1, rowIndex + 1):
        result.append(current_numerator // current_factorial)
        current_numerator *= (rowIndex - i)
        current_factorial *= i + 1

    return result


# [1] + [reduce(mul, [rowIndex - j for j in range(i)]) // factorial(i) for i in range(1, rowIndex + 1)]


lst = []


def get_row(row: int) -> List[int]:
    if row == 0:
        return []
    elif row == 1:
        return [1]
    elif row == 2:
        return [1, 1]

    result = get_row(row - 1)
    for i in range(len(result) - 1):
        result[i] = result[i] + result[i + 1]
    return [1] + result


# functools.reduce(operator.mul, [n - i for i in range(n)], 1) // math.factorial(n)

print(get_row(5))
