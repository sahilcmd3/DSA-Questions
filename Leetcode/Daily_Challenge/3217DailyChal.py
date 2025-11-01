# Delete Nodes From Linked List Present in Array

"""You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes
from the linked list that have a value that exists in nums."""

from __future__ import annotations
from typing import final, override


@final
class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next

    @override
    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def modifiedList(self, nums: list[int], head: ListNode | None) -> ListNode | None:
        hs = set(nums)
        cur = head
        prev: ListNode | None = None

        while cur:
            next_node = cur.next
            if cur.val in hs:
                if cur is head:
                    head = next_node
                else:
                    assert prev is not None
                    prev.next = next_node
            else:
                prev = cur
            cur = next_node

        return head


# --- Helpers for quick testing ---
def build_list(values: list[int]) -> ListNode | None:
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def to_pylist(head: ListNode | None) -> list[int]:
    out: list[int] = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


if __name__ == "__main__":
    s = Solution()

    head = build_list([1, 2, 3, 4, 5, 2])
    print("before:", to_pylist(head))

    head = s.modifiedList([2, 5], head)
    print("after: ", to_pylist(head))

    # remove everything
    head = build_list([7, 7, 7])
    head = s.modifiedList([7], head)
    print("all removed ->", head)
