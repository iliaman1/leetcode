from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def remove_leaf_nodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.remove_leaf_nodes(root.left, target)
        root.right = self.remove_leaf_nodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            root = None

        return root
