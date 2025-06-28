"""The height of a binary tree is the number of edges between the tree's root and its furthest leaf."""

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def height(root):
    if root is None:
        return -1

    return 1 + max(height(root.left), height(root.right))
