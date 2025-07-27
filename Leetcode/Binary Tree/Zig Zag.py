# LEETCODE 103

"""Intuition
To perform a zigzag level order traversal of a binary tree, we alternate between left-to-right and right-to-left processing at each level.
Using a deque (double-ended queue) allows efficient popping and pushing from both ends to handle the direction change naturally.

Approach
Use a deque to store nodes of each level.
Use a boolean flag reverse to toggle direction.
If reverse == false:
Poll nodes from the front of deque, add their children left → right to the back.
If reverse == true:
Poll nodes from the back, add their children right → left to the front.
Toggle reverse after each level."""

from collections import deque


def zigzag(root):
    if not root:
        return

    res = []
    dq = deque([root])
    reverse = False

    while dq:
        level = []
        for _ in range(len(dq)):
            if not reverse:
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            else:
                node = dq.pop()
                level.append(node.val)
                if node.right:
                    dq.appendleft(node.right)
                if node.left:
                    dq.appendleft(node.left)

        res.append(level)
        reverse = not reverse

    return res
