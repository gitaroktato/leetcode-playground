# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # init - once
        self.levels = []
        self.traverse(0, root)
        return self.levels

    def traverse(self, level: int, root: Optional[TreeNode]):
        if root is None:
            return
        # add a new level
        if len(self.levels) <= level:
            self.levels.append([])
        # add the root
        self.levels[level].append(root.val)
        self.traverse(level + 1, root.left)
        self.traverse(level + 1, root.right)
