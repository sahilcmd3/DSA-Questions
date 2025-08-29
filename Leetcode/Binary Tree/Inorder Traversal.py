# LEETCODE 94

"""Given the root of a binary tree, return the inorder traversal of its nodes' values."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive approach
# L N R
def inorderTrav(root):
    result = []

    def inorder(node):
        if not node:  # Base case to stop the recursive traversing (also means reaching the end of a subtree)
            return

        inorder(node.left)  # L
        result.append(node.val)  # N (ye append isliye hua hai ku ki subtrees ka root node hi main ya left node hota hai)
        inorder(node.right)  # R

    inorder(root)
    return result


# Iteratively (stack)
def inorder(root):
    res = []
    stack = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        res.append(root.val)
        root = root.right

    return res
