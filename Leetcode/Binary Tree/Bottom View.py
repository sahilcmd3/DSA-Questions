# GFG Bottom View of a Binary Tree

"""Given a binary tree, return an array where elements represent the bottom view of the binary tree from left to right.

Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the later one in the level order 
traversal is considered. For example, in the below diagram, 7 and 34 both are the bottommost nodes at a horizontal distance of 0 from the root, 
here 34 will be considered."""


from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def bottomView(self, root):
        if not root:
            return []

        # Dictionary to store the last node at each horizontal distance
        hd_map = {}
        queue = deque([(root, 0)])  # (node, horizontal distance)

        while queue:
            node, hd = queue.popleft()

            # Overwrite the value at horizontal distance with the latest one
            hd_map[hd] = node.data
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        # Extract values in order of increasing horizontal distance
        return [hd_map[hd] for hd in sorted(hd_map)]
