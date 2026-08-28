class Solution:
    # Sliding window starting from left
    # k different chars can be skipped
    # if k depleted change window to 1
    # jump to left+1 and continue
    # Complexity: n2
    #
    # Optimization: jump to first different char+1
    # Set current replacement available+1
    def characterReplacement(self, s: str, k: int) -> int:
        window_left: int = 0
        window_right: int = 0
        remaining_replacements: int = 0
        while window_right < len(s):
            if s[window_right] == s[window_left]:
                window_right += 1
            elif remaining_replacements < k:
                # We still have replacements to go
                remaining_replacements += 1
                window_right += 1
            else:
                # Jump to first different char+1
                # Set current replacement avail+1
                
        return window_right - window_left
