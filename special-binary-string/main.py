class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        return "11110100"

    # do_swap - assertion for special string
    # is_special(substr) - true/false
    # get_all_specials -> list of indexes (with length, with lexiographical rank)
    # lexiographical rank: number of 1s as prefix.
    # {index: 1, length: 2, number_of_ones: 1}
