# Reverse Linked List 2

"""Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes
of the list from position left to position right, and return the reversed list."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity: O(n)
class Solution:
    def revBetween(self, head, left, right):
        if not head or left == head:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
