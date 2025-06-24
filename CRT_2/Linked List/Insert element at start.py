# Node class to represent a linked list node
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next  # Dot is the attribute access operator 

# Function to insert a new node at the head of the linkedlist
def insertHead(head, val):
    temp = Node(val, head)
    return temp


if __name__ == "__main__":
    arr = [12, 6, 7, 7]
    val = 100

    # Creating a linked list with initial elements from the array
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    # Inserting a new node at the head of the linked list
    head = insertHead(head, val)
    printLL(head)
