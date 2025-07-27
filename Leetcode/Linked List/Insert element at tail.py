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


def insertEnd(head, val):
    new_node = Node(val)
    if head is None:
        return new_node

    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = new_node

    return head


if __name__ == "__main__":
    arr = [12, 6, 7, 7]
    val = 100

    head = None
    for value in arr:
        if head is None:
            head = Node(value)
            temp = head
        else:
            temp.next = Node(value)
            temp = temp.next

    head = insertEnd(head, val)
    printLL(head)
