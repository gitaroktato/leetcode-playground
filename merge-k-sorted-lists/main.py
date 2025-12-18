from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.next == other.next

    def to_list(self):
        result = []
        node = self
        while node:
            result.append(node.val)
            node = node.next
        return result


def build_list(arr):
    head = ListNode(0)
    curr = head
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return head.next


def get_min_index(lists: List[Optional[ListNode]]) -> int:
    min_index = -1
    for i in range(len(lists)):
        node = lists[i]
        if not node:
            continue
        elif min_index == -1:
            min_index = i
        elif lists[min_index].val > node.val:
            min_index = i
    return min_index


# TODO: iterate over list of nodes


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_first: Optional[ListNode] = None
        merged_current: Optional[ListNode] = None
        min_index = get_min_index(lists)
        while min_index != -1:
            if not merged_first and not merged_current:
                merged_first = lists[min_index]
                merged_current = merged_first
            else:
                merged_current.next = lists[min_index]
                merged_current = merged_current.next
            lists[min_index] = lists[min_index].next
            min_index = get_min_index(lists)
        return merged_first
