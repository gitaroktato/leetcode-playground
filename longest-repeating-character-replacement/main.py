class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window starting from left
        # k different chars can be skipped
        # if k depleted change window to 1
        # jump to left+1 and continue
        # Complexity: n2
        #
        # Optimization: jump to first different char+1
        # Set current replacement available+1
        return 0
