# Remove Nth Node From End of List

"""Given the head of a linked list, remove the nth node from the end of the list and return its head."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity: O(n)
class Solution:
    def removeNth(self, head, n):
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next

        return res.next
