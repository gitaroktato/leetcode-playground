from typing import List, NamedTuple


class HeightAtIndex(NamedTuple):
    i: int
    height: int


def calculate_area(base: int, until: int, height: int) -> int:
    return (until - base) * height


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # initialization
        curr_max = 0
        stack: List[HeightAtIndex] = []
        for i, height in enumerate(heights):
            if stack and height < stack[-1].height:
                while True:
                    # pop array
                    last_height = stack.pop()
                    # calcullate max
                    new_area = calculate_area(last_height.i, i, last_height.height)
                    curr_max = max(new_area, curr_max)
                    if not stack:
                        stack.append(HeightAtIndex(last_height.i, height))
                        break
                    if height >= stack[-1].height:
                        stack.append(HeightAtIndex(last_height.i, height))
                        break
            else:
                stack.append(HeightAtIndex(i, height))
        # TODO final height
        last_index = len(heights)
        while stack:
            # pop array
            last_height = stack.pop()
            # calcullate max
            new_area = calculate_area(last_height.i, last_index, last_height.height)
            curr_max = max(new_area, curr_max)
            # last_index = last_height.i
        return curr_max
