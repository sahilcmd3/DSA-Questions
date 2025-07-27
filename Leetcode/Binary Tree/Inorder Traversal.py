# LEETCODE 94

"""Given the root of a binary tree, return the inorder traversal of its nodes' values."""

# Iteratively khud krna h (stack)
# Recursive approach
# L N R


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTrav(root):
    result = []

    def inorder(node):
        if not node:
            return

        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result
