# Rotate List

"""Given the head of a linked list, rotate the list to the right by k places."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity: O(n)
class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        length = 1
        dummy = head

        while dummy.next:
            dummy = dummy.next
            length += 1

        position = k % length
        if position == 0:
            return head

        current = head

        for _ in range(length - position - 1):
            current = current.next

        new_head = current.next
        current.next = None
        dummy.next = head

        return new_head
