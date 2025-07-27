# LEETCODE 199

"""Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
you can see ordered from top to bottom."""

from collections import deque


# Level Order approach
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # Capture the rightmost node at this level
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


# DFS Recursive approach
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        result = []

        def dfs(node, level):
            if not node:
                return
            # If this is the first node we're visiting at this level
            if level == len(result):
                result.append(node.val)
            # Prioritize right subtree to capture rightmost nodes
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return result
