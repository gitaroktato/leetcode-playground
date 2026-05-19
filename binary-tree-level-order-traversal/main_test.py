from main import Solution, TreeNode


def test_level_order_traversal():

    solution = Solution()
    level_order_func = solution.levelOrder

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = level_order_func(root)
    print(result)
    assert result == [[3], [9, 20], [15, 7]]
