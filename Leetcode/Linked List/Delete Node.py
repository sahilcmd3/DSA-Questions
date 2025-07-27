class Node:
    def __init__(self, x):
        self.x = x
        self.next = None


# Time complexity: O(1)
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
