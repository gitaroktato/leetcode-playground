from main import Solution


def test_merge():
    sol = Solution()
    assert sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_merge_again():
    sol = Solution()
    assert sol.merge([[4, 7], [1, 4]]) == [[1, 7]]


def test_merge_again_again():
    sol = Solution()
    assert sol.merge([[1, 4], [2, 3]]) == [[1, 4]]
