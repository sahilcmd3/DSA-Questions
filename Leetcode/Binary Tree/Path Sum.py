# LEETCODE 112

"""Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all
the values along the path equals targetSum.
A leaf is a node with no children."""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        # Check if it's a leaf node
        if not root.left and not root.right:
            return root.val == targetSum

        # Recurse on left and right subtrees with updated targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )
