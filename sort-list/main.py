# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return mergeSort(head)


def split(head):
    fast = head
    slow = head

    # Move fast pointer two steps and slow pointer
    # one step until fast reaches the end
    while fast and fast.next:
        fast = fast.next.next
        if fast:
            slow = slow.next

    # Split the list into two halves
    second = slow.next
    slow.next = None
    return second


def merge(first: Optional[ListNode], second: Optional[ListNode]):
    # If either list is empty, return the other list
    if not first:
        return second
    if not second:
        return first

    # Pick the smaller value between first and second nodes
    if first.val < second.val:
        first.next = merge(first.next, second)
        return first
    else:
        second.next = merge(first, second.next)
        return second


def mergeSort(head: Optional[ListNode]):
    # Base case: if the list is empty or has only one node,
    # it's already sorted
    if not head or not head.next:
        return head

    # Split the list into two halves
    second = split(head)

    # Recursively sort each half
    head = mergeSort(head)
    second = mergeSort(second)

    # Merge the two sorted halves
    return merge(head, second)
