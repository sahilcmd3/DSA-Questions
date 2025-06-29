# GFG Left View of Binary tree

# Level order bfs approach
from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def LeftView(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
    
            if i == 0:
                result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


# DFS with recursion
def LeftView(self, root):
    result = []

    def dfs(node, level):
        if not node:
            return

        # If this is the first node we're visiting at this level
        if level == len(result):
            result.append(node.data)

        # Prioritize left subtree to ensure leftmost nodes are visited first
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result
