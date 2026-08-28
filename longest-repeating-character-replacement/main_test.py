from main import Solution


def test_main():
    sol = Solution()
    res = sol.characterReplacement("AAB", 1)
    assert res == 3
