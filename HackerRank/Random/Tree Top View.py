"""Given a pointer to the root of a binary tree, print the top view of the binary tree.
The tree as seen from the top the nodes, is called the top view of the tree."""


from collections import deque


class Node:
    def __init__(self, left, right, info):
        self.left = left
        self.right = right
        self.info = info


def topView(root):
    if not root:
        return

    q = deque([(root, 0)])
    hd_map = {}

    while q:
        node, hd = q.popleft()
        if hd not in hd_map:
            hd_map[hd] = node.info
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))

    for hd in sorted(hd_map):
        print(hd_map[hd], end=" ")
        