# LEETCODE 102

"""Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)."""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    result = []

    if not root:
        return result

    q = deque([root])
    while q:
        same_level = []
        for _ in range(len(q)):
            node = q.popleft()
            same_level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(same_level)

    return result


"""BFS Traversal
The BFS traversal uses a while loop that continues until the queue is empty. Inside the loop:

 - Track Nodes at the Same Level:
    - A temporary list, same_level, is created to store node values for the current level.

 - Process Nodes in the Queue:
    - For each node in the current level (determined by len(q)), we:
        - Remove the node from the queue (q.popleft()).
        - Append its value to same_level.
        - Add its left and right children (if they exist) to the queue.

 - Store Level Values:
    - After processing all nodes in the current level, same_level is appended to the result list res."""
