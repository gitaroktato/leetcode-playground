from typing import List


def get_area_in_inc(inc_stack: list[int]) -> int:
    if not inc_stack:
        return 0
    width = 0
    size = 0
    height = inc_stack[-1]
    for element in reversed(inc_stack):
        width += 1
        height = min(height, element)
        size = max(size, width * height)
    return size


def get_area_in_dec(dec_stack: list[int]) -> int:
    if not dec_stack:
        return 0
    width = 0
    size = 0
    height = dec_stack[0]
    for element in dec_stack:
        width += 1
        height = min(height, element)
        size = max(size, width * height)
    return size


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        inc_stack = []
        dec_stack = []
        max_area = 0
        for idx, elem in enumerate(heights):
            if idx == 0 or elem == heights[idx - 1]:
                inc_stack.append(elem)
                dec_stack.append(elem)
            elif elem < heights[idx - 1]:
                # decreasing
                dec_stack.append(elem)
                area = get_area_in_inc(inc_stack)
                max_area = max(max_area, area)
                inc_stack = []
            elif elem > heights[idx - 1]:
                # decreasing
                inc_stack.append(elem)
                area = get_area_in_dec(dec_stack)
                max_area = max(max_area, area)
                dec_stack = []
        if inc_stack:
            area = get_area_in_inc(inc_stack)
            max_area = max(max_area, area)
        if dec_stack:
            area = get_area_in_dec(dec_stack)
            max_area = max(max_area, area)
        return max_area
