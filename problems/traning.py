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


def caching(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if args[1] in cache:
            return cache[args[1]]
        cache[args[1]] = func(args[0], args[1])
        print(cache)
        return func(args[0], args[1])

    return wrapper


class FibSolution:

    @caching
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        return self.fib(n - 1) + self.fib(n - 2)


class ClimbStairsSolution:
    @caching
    def climb_stairs(self, n: int) -> int:
        if n < 3:
            return n

        return self.climb_stairs(n - 1) + self.climb_stairs(n - 2)


class SolutionMaxDepth:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 0 if root == None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


def myPow(x: float, n: int) -> float:
    def pow(x: float, n: int) -> float:
        if x == 0:
            return 0

        if n == 0:
            return 1

        if n == 1:
            return x

        result = pow(x, n // 2)
        result *= result

        return result if n % 2 == 0 else x * result

    return pow(x, n) if n > 0 else 1 / pow(x, abs(n))


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 and list2:
        if list1.val <= list2.val:
            head, list1 = list1, list1.next
        else:
            head, list2 = list2, list2.next

        head.next = mergeTwoLists(list1, list2)

        return head

    else:
        return list1 or list2




