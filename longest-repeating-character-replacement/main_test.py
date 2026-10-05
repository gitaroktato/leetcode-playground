from main import Solution


def test_main_with_all_matching():
    sol = Solution()
    res = sol.characterReplacement("AAAAA", 0)
    assert res == 5


def test_main():
    sol = Solution()
    res = sol.characterReplacement("AAB", 1)
    assert res == 3


def test_main_with_xy():
    sol = Solution()
    res = sol.characterReplacement("XYYX", 2)
    assert res == 4


def test_main_with_longer_text():
    sol = Solution()
    res = sol.characterReplacement("AAABABB", 1)
    assert res == 5


def test_main_with_k1_and_jump():
    sol = Solution()
    res = sol.characterReplacement("AABABBAABAA", 1)
    assert res == 5
