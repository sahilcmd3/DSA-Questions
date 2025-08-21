# Reverse Nodes in k-Group (Hard)

"""Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k
then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity: O(n)
class Solution:
    def revKgrp(self, head, k):
        if not head:
            return None

        tail = head

        for _ in range(k):
            if not tail:
                return head
            tail = tail.next

        def reverse(cur, end):
            prev = None

            while cur != end:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next

            return prev

        new_head = reverse(head, tail)
        head.next = self.reverseKGroup(tail, k)

        return new_head
