# LEETCODE 83


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplic(head):
    res = head

    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next

    return res
