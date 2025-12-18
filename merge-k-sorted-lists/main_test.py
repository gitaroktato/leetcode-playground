import pytest
from main import ListNode, Solution, get_min_index


def build_list(arr):
    head = ListNode(0)
    curr = head
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return head.next


def to_list(node: ListNode | None) -> list[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


s = Solution()


def test_merge_k_lists_basic():
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    merged = s.mergeKLists(lists)
    assert to_list(merged) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_merge_k_lists_empty():
    lists = []
    merged = s.mergeKLists(lists)
    assert merged is None


def test_merge_k_lists_all_empty():
    lists = [None, None]
    merged = s.mergeKLists(lists)
    assert merged is None


def test_merge_k_lists_single_list():
    lists = [build_list([1, 2, 3])]
    merged = s.mergeKLists(lists)
    assert to_list(merged) == [1, 2, 3]


def test_merge_k_lists_lists_with_empty():
    lists = [build_list([2]), None, build_list([1])]
    merged = s.mergeKLists(lists)
    assert to_list(merged) == [1, 2]


@pytest.mark.parametrize(
    "input_lists,expected_index",
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], 0),
        ([[2, 4], [1, 3], [5, 6]], 1),
        ([[3], [2], [1]], 2),
        ([[5], [5], [5]], 0),
        ([None, [1], [2]], 1),
        ([None, None, [0]], 2),
    ],
)
def test_get_min_index(input_lists, expected_index):
    lists = [build_list(lst) if lst is not None else None for lst in input_lists]
    index = get_min_index(lists)
    assert index == expected_index
