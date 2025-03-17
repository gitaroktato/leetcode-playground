from main import Solution


def test_main():
    sol = Solution()
    res = sol.lengthOfLongestSubstring("pwwkew")
    assert res == 3


def test_main_with_empty():
    sol = Solution()
    res = sol.lengthOfLongestSubstring("")
    assert res == 0


def test_main_with_ne():
    sol = Solution()
    res = sol.lengthOfLongestSubstring("dvdf")
    assert res == 3


def test_main_with_nex():
    sol = Solution()
    res = sol.lengthOfLongestSubstring("abcabcbb")
    assert res == 3
