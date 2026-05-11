from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            left, right = interval[0], interval[1]
            if len(merged) == 0:
                merged.append([left, right])
            if len(merged) != 0:
                before_left, before_right = merged[-1][0], merged[-1][1]
                # overlappin
                if before_right >= left:
                    merged[-1][1] = max(right, before_right)
                else:
                    merged.append([left, right])
        return merged
