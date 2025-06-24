class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def printLL(head):
    while head is not None:
        if head.next:
            print(head.data, end=" -> ")
        else:
            print(head.data, end=" -> None")
        head = head.next


def deleteEnd(head):
    # Edge case: Checking if linked list is empty or has only one Node
    if head is None or head.next is None:
        return None

    # A temp pointer for traversal
    temp = head

    # traverse till second to last node
    while temp.next.next is not None:
        temp = temp.next

    # Nullify the connection from the second-to-last node to delete the last node
    temp.next = None

    return head


if __name__ == "__main__":
    arr = [12, 3, 4, 5]

    head = None
    for value in arr:
        if head is None:
            head = Node(value)
            temp = head
        else:
            temp.next = Node(value)
            temp = temp.next

    head = deleteEnd(head)
    printLL(head)
