class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(node, is_left=False):
            if not node:
                return 0

            if not node.left and not node.right and is_left:
                return node.val

            left_sum = helper(node.left, True)
            right_sum = helper(node.right)

            return left_sum + right_sum

        return helper(root)
