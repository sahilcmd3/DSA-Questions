# LEETCODE 82


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def deleteDupli(head):
    freq = {}
    curr = head
    while curr:
        freq[curr.val] = freq.get(curr.val, 0) + 1
        curr = curr.next

    dummy = Node(0)
    tail = dummy
    curr = head
    while curr:
        if freq[curr.val] == 1:
            tail.next = Node(curr.val)
            tail = tail.next
        curr = curr.next

    return dummy.next
