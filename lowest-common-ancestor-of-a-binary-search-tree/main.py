# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None

    def __str__(self) -> str:
        return f"{self.val} -> {self.left}, -> {self.right}"

    def __repr__(self) -> str:
        return str(self)


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        lowest_common = root
        if p.val < root.val and q.val < root.val:  # left
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:  # right
            return self.lowestCommonAncestor(root.right, p, q)
        return lowest_common
