# Intersection of Two Linked Lists

"""Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists
have no intersection at all, return null."""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Time complexity: O(m+n)
def getIntersectionNode(headA, headB):
    lista = headA
    listb = headB

    while lista != listb:
        # If lista is not None, it moves to the next node (lista.next). Otherwise, it switches to the head of the other list (headB)
        lista = lista.next if lista else headB
        # If listb is not None, it moves to the next node (listb.next). Otherwise, it switches to the head of the other list (headA)
        listb = listb.next if listb else headA
        # Why the switch?
        # When a pointer reaches the end of one list and switches to the other, the difference in lengths between the two lists is
        # neutralized. This ensures that both pointers traverse the same total distance before meeting.

    return listb
