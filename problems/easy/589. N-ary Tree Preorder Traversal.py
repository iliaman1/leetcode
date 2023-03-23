class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def tree_to_list(self, current_node, res: list = []) -> None:
        if current_node:
            res.append(current_node.val)
            for i in current_node.children:
                self.tree_to_list(i, res)

    def preorder(self, root: Node) -> list[int]:
        res = []
        self.tree_to_list(root, res)
        return res
