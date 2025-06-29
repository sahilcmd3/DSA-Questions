# LEETCODE 145

"""Given the root of a binary tree, return the postorder traversal of its nodes' values."""

# L R N
# Recursive
# Iteratively khud krna h (stack)


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def postOrderTrav(root):
    result = []

    def postorder(node):
        if not node:
            return

        postorder(node.left)
        postorder(node.right)
        result.append(node.val)

    postorder(root)

    return result
