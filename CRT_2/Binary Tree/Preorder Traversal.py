# LEETCODE 144

"""Given the root of a binary tree, return the preorder traversal of its nodes' values."""

# N L R
# Recursive
# Iteratively khud krna h (stack)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTrav(root):
    result = []

    def preorder(node):
        if not node:
            return

        result.append(node.val)
        preorder(node.left)
        preorder(node.right)

    preorder(root)

    return result
