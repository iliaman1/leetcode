from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sum_numbers(self, root: Optional[TreeNode], num: int = 0) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return num * 10 + root.val

        return self.sum_numbers(root.left, num * 10 + root.val) + self.sum_numbers(root.right, num * 10 + root.val)
