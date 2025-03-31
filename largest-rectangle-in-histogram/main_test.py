from main import get_area_in_inc, get_area_in_dec, Solution


def test_get_area_in_inc():
    stack = [2]
    assert get_area_in_inc(stack) == 2


def test_get_area_in_inc_more():
    stack = [1, 5, 6]
    assert get_area_in_inc(stack) == 10


def test_get_area_in_dec():
    stack = [2]
    assert get_area_in_dec(stack) == 2


def test_get_area_in_dec_more():
    stack = [6, 5, 1]
    assert get_area_in_dec(stack) == 10


def test_get_heights():
    heights = [2, 4]
    assert Solution().largestRectangleArea(heights) == 4


def test_get_heights_again():
    heights = [2, 1, 5, 6, 2, 3]
    assert Solution().largestRectangleArea(heights) == 10


def test_get_heights_again2():
    heights = [2, 1, 2]
    assert Solution().largestRectangleArea(heights) == 3
