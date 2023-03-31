class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # long
    def max_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_branch = self.max_depth(root.left)
            right_branch = self.max_depth(root.right)
        return max(left_branch, right_branch) + 1

    # short
    def max_depth_short(self, root: TreeNode) -> int:
        return max(self.max_depth_short(root.left), self.max_depth_short(root.right)) + 1 if root else 0
