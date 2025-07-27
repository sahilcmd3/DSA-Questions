"""Given a pointer to the head of a linked list and a specific position, determine the data value at that position. Count backwards
from the tail node. The tail is at postion 0, its parent is at 1 and so on."""


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def getNode(llist, positionFromTail):
    values = []

    while llist:
        values.append(llist.data)
        llist = llist.next

    return values[-(positionFromTail + 1)]
