# Partition List

"""Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.


Explaination:
Basically, it asks us:
reorder the sequence by the given number x

The rules are:

    Any number that is less than x has to be before x, and maintain the relative order with thoese that are less than x but already before x.
    e.g. [3,4,1,2], target = 4 -> [3,1,2,4], so the order of [3,1,2] is maintained.

    Any number that is greater than x but already before x will still be before x, but all of them come after those that are less
    than x and at the same time maintain their relative order.
    e.g. [3,6,5,4,1,2] target = 4 -> [3,1,2,6,5,4]

    Any number that is greater than x and after x will only need to maintain their relative order
    e.g. [3,6,5,4,8,1,7,2] target = 4 -> [3,1,2,6,5,4,8,7]

Hope this helps those who have a difficulty time understanding "all nodes less than x come before nodes greater than or equal to x." like me.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity: O(n)
class Solution:
    def partition(self, head, x):
        less_head = ListNode(0)  # Sirf head banaye hain dummy & less_head for nodes < x
        greater_head = ListNode(0)  # greater_head for nodes >= x
        less = less_head
        greater = greater_head

        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

        greater.next = None  # After traversal, terminates the “greater” list with greater.next = None (prevents accidental cycles).
        less.next = greater_head.next  # Connecting lists

        return less_head.next


def list_to_linkedlist(vals):
    dummy = ListNode(0)
    curr = dummy

    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next

    return dummy.next


def linkedlist_to_list(head):
    out = []

    while head:
        out.append(head.val)
        head = head.next

    return out


if __name__ == "__main__":
    vals = [1, 4, 3, 2, 5, 2]
    x = 3
    head = list_to_linkedlist(vals)
    res_head = Solution().partition(head, x)
    print("Input:", vals, "x =", x)
    print("Output:", linkedlist_to_list(res_head))
