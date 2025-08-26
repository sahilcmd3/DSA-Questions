"""A tree is a fundamental data structure in computer science that represents a hierarchical structure. It consists of
  nodes connected by edges, forming a branching structure similar to a real-life tree.

* ### Key Features of a Tree:
   - Root Node: The topmost node, serving as the entry point.
   - Child Nodes: Nodes directly connected to another node.
   - Parent Node: A node that has child nodes.
   - Leaf Nodes: Nodes without children.
   - Depth: The length of the path from the root to a node.
   - Height: The longest path from a node to a leaf.

* ### Types of Trees:
   - Binary Tree: Each node has at most two children.
   - Binary Search Tree (BST): A binary tree with ordered nodes for efficient searching.
   - Balanced Tree: Ensures equal distribution of nodes for optimal performance.
   - Trie: Used for fast prefix-based searching, often in dictionaries.
   - Heap: A complete binary tree used in priority queues.
   - Ternary Tree: A Ternary Tree is a tree data structure in which each node has at most three child nodes, usually
     distinguished as “left”, “mid” and “right”.
   - N-ary Tree or Generic Tree: Generic trees are a collection of nodes where each node is a data structure that consists
     of records and a list of references to its children(duplicate references are not allowed). Unlike the linked list,
     each node stores the address of multiple nodes.

* Binary Tree: Each node has at most two children.

* ### Types of Binary Tree:
   - Complete Binary Tree: A binary tree in which every level, except possibly the last, is completely filled, and all
     nodes are as far left as possible. For example, a heap is a complete binary tree that satisfies the heap property
     (either max-heap or min-heap).

   - Full Binary Tree: A binary tree where every node has either 0 or 2 children.

   - Degenerate Binary Tree (or Pathological Tree): A tree in which each parent node has only one child. This
     essentially forms a linked list, which leads to inefficient operations.

   - Binary Search Tree (BST) and its Variations: A BST is a binary tree where each node has at most two children,
     and for each node, the left child’s value is smaller than the node’s value, and the right child’s value is greater.
     An AVL Tree is a self-balancing BST where the heights of the two child subtrees of any node differ by no more than one.
     Red Black Tree and Splay Tree are more example variations of BST.

   - Binary Indexed Tree (Fenwick Tree): A data structure that uses a binary tree to efficiently compute and update prefix
     sums in an array.

   - Perfect Binary Tree: A binary tree where all internal nodes have two children and all leaf nodes are at the same level.
       - No. of nodes at (L) level : 2^L
       - No. of nodes total (at h) : 2^h-1

   - Balanced Binary Tree: A binary tree where the difference in heights between the left and right subtrees of any
     node is minimal (often defined as at most 1). Examples of Balanced Binary Tree are AVL Tree, Red Black Tree and Splay Tree

   - Segment Tree: A segment tree is a binary tree used for storing intervals or segments. It allows efficient querying
     and updating of ranges of values, making it particularly useful for problems that involve finding the sum, minimum,
     maximum, or other operations over a range of elements in an array.

* ### DFS (Depth-First Search) and BFS (Breadth-First Search) are tree traversal strategies, whereas
      preorder, inorder, and postorder are specific types of DFS traversal.

* ### DFS vs. BFS
 - DFS (Depth-First Search):
   - Goes deep into the tree first before backtracking.
   - Uses recursion or a stack.
   - Three main types: preorder, inorder, and postorder.

 - BFS (Breadth-First Search):
   - Explores level by level, visiting all nodes at the same depth before moving deeper.
   - Uses a queue to store nodes at each level.

* ### Preorder, Inorder, Postorder (DFS Variations)
 These are specific ways DFS is performed:
   1. Preorder (Root → Left → Right)
   2. Inorder (Left → Root → Right)
   3. Postorder (Left → Right → Root)

* ### Comparison
 | Traversal  | Type        | Order of Visit      | Use Case                                     |
 |------------|-------------|---------------------|----------------------------------------------|
 | DFS        | Strategy    | Goes deep first     | Useful for backtracking, tree-based problems |
 | BFS        | Strategy    | Goes level by level | Best for shortest path finding               |
 | Preorder   | DFS Variant | Root → Left → Right | Used for copying or reconstructing trees     |
 | Inorder    | DFS Variant | Left → Root → Right | Used for sorted binary trees                 |
 | Postorder  | DFS Variant | Left → Right → Root | Used for deleting or evaluating trees        |

* ### Key Insight
 - DFS is an approach, and preorder/inorder/postorder are just different variations of DFS.
 - BFS follows a completely different level-based approach, rather than going deep first.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def create_perfect_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root


# BFS using a queue
from collections import deque


def bfs_q(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data, end="\t")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# BFS without a queue (level-order traversal)
def get_height(root):
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


def print_level(root, level):
    if not root:
        return
    if level == 1:
        print(root.data, end="\t")
    else:
        print_level(root.left, level - 1)
        print_level(root.right, level - 1)


def bfs(root):
    height = get_height(root)
    for i in range(1, height + 1):
        print_level(root, i)


# DFS (Preorder Traversal)
def dfs(root):
    if not root:
        return
    print(root.data, end="\t")
    dfs(root.left)
    dfs(root.right)


# Inorder Traversal (Left -> Root -> Right)
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end="\t")
    inorder(root.right)


# Postorder Traversal (Left -> Right -> Root)
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end="\t")


def print_tree():
    root = create_perfect_tree()

    print("BFS (Level Order): ", end="")
    bfs(root)
    print("\n")

    print("Preorder Traversal (DFS): ", end="")
    dfs(root)
    print("\n")

    print("Inorder Traversal: ", end="")
    inorder(root)
    print("\n")

    print("Postorder Traversal: ", end="")
    postorder(root)
    print("\n")


if __name__ == "__main__":
    print_tree()