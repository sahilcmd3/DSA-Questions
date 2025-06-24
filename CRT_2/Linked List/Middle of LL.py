# LEETCODE 876


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity: O(n)
def middleNode(head):
    slow = fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next  # Go to the object that slow is referring to, and fetch its next attribute
        fast = fast.next.next

    return slow
