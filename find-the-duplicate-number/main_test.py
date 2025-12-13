import pytest
from main import Solution

s = Solution()


def test_single_duplicate():
    nums = [1, 3, 4, 2, 2]
    assert s.findDuplicate(nums) == 2


def test_duplicate_at_start():
    nums = [3, 1, 3, 4, 2]
    assert s.findDuplicate(nums) == 3


def test_multiple_duplicates():
    nums = [2, 2, 2, 2, 2]
    assert s.findDuplicate(nums) == 2


def test_large_input():
    nums = list(range(1, 10000)) + [9999]
    assert s.findDuplicate(nums) == 9999
