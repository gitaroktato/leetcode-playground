# 424. Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# Example 1: s = "ABAB", k = 2 -> Output: 4 (Replace the two 'A's with two 'B's or vice versa.)
# Example 2: s = "AABABBA", k = 1 -> Output: 4 (The substring "BBBB" has the longest repeating letters, which is 4.)
# Constraints: 1 <= s.length <= 10^5; s consists of only uppercase English letters; 0 <= k <= s.length


class Solution:
    # Sliding window starting from left
    # k different chars can be skipped
    # if k depleted change window to 1
    # jump to left+1 and continue
    # Complexity: n2
    #
    # Optimization: jump to first different char+1
    # Set current replacement available+1
    # TODO: Use-case that's moving the left window more on conditions
    def characterReplacement(self, s: str, k: int) -> int:
        window_left: int = 0
        window_right: int = 0
        remaining_replacements: int = 0
        last_change = 0
        longest_found = 0
        while window_right < len(s):
            if s[window_right] == s[window_left]:
                window_right += 1
            elif remaining_replacements < k:
                # We still have replacements to go
                remaining_replacements += 1
                last_change = window_right
                window_right += 1
            else:
                # Jump to first different char+1
                # Set current replacement avail+1
                longest_found = max(window_right - window_left, longest_found)
                window_left = last_change if k > 0 else window_right
                window_right = window_left
                remaining_replacements = 0
                last_change = window_left

        longest_found = max(window_right - window_left, longest_found)
        return longest_found
