class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_branch = self.max_depth(root.left)
            right_branch = self.max_depth(root.right)
        return max(left_branch, right_branch) + 1
