from main import Solution


def test_get_heights():
    heights = [2, 4]
    assert Solution().largestRectangleArea(heights) == 4


def test_get_heights_again():
    heights = [2, 1, 5, 6, 2, 3]
    assert Solution().largestRectangleArea(heights) == 10


def test_get_heights_again2():
    heights = [2, 1, 2]
    assert Solution().largestRectangleArea(heights) == 3
