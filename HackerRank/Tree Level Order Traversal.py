"""Given a pointer to the root of a binary tree, you need to print the level order traversal of this tree. In level-order traversal,
nodes are visited level by level from left to right. Complete the function levelOrder and print the values in a single line separated
by a space."""


from collections import deque


class Node:
    def __init__(self, left, right, info):
        self.left = left
        self.right = right
        self.info = info


def levelOrder(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.info, end=" -> ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
