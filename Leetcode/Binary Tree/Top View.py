# GFG Top view of binary tree

"""You are given a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible
when the tree is viewed from the top.

Note:
Return the nodes from the leftmost node to the rightmost node.
If two nodes are at the same position (horizontal distance) and are outside the shadow of the tree, consider the leftmost node only.
"""


# Solved using vertical positioning approach here the root node in the middle is 0
"""       0=root0     
    -1=node1   node2=1
          0=node3
-2=node4           node5=2  """
# don't select 0's

from collections import deque


# Definition for a binary tree node.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def topview(root):
    ans = []
    if not root:
        return ans

    q = deque([(root, 0)])
    mp = dict()

    while q:
        node, pos = q.popleft()

        if pos not in mp:
            mp[pos] = node.data
        if node.left:
            q.append((node.left, pos - 1))
        if node.right:
            q.append((node.right, pos + 1))

    for key in sorted(mp):
        ans.append(mp[key])

    return ans
