from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def add_one_row(self, root: Optional[TreeNode], val: int, depth: int, current: int = 1) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root

            return new_root

        if not root:
            return None

        if current == depth - 1:
            ltemp = root.left
            rtemp = root.right

            root.left = TreeNode(val)
            root.right = TreeNode(val)
            root.left.left = ltemp
            root.right.right = rtemp

            return root

        root.left = self.add_one_row(root.left, val, depth, current + 1)
        root.right = self.add_one_row(root.right, val, depth, current + 1)

        return root
