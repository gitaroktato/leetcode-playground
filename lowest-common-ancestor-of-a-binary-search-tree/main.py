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
        if root.right is not None and root.right.val > p.val and root.right.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.left is not None and root.left.val < p.val and root.left.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return lowest_common
