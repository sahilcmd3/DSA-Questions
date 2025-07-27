# LEETCODE 2


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# Time Complexity: O(max(m, n)) — where m and n are the lengths of the two lists.
def addTwoNums(l1, l2):
    dummy = Node()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = Node(total % 10)

        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next
