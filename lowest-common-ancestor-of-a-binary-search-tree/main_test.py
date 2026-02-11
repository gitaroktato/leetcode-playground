import sys

sys.path.append(".")

from main import Solution, TreeNode

solution = Solution()
lca_func = solution.lowestCommonAncestor


def build_test_tree():
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    return root


def test_lowest_common_ancestor():
    root = build_test_tree()
    lca = lca_func(root, root.left, root.right)
    assert lca.val == 6


def test_lowest_common_ancestor_2():
    root = build_test_tree()
    lca_lower = lca_func(root, root.left.left, root.left.right)
    assert lca_lower.val == 2


def test_lowest_common_ancestor_3():
    root = build_test_tree()
    lca_lower = lca_func(root, root.left, root.left.right)
    assert lca_lower.val == 2
