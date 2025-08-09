# Copy List with Random Pointer

"""A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in
the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to
the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied
list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should
point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the
copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list."""


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Time complexity: O(n)
class Solution:
    def copyRandomList(self, head):
        hash = {None: None}
        cur = head

        while cur:
            hash[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur:
            copy = hash[cur]
            copy.next = hash[cur.next]
            copy.random = hash[cur.random]
            cur = cur.next

        return hash[head]


"""
    Create a dictionary (hash) to map original nodes to their corresponding copied nodes.
        Initialize the dictionary with a mapping of None to None.

    Traverse the original linked list using a pointer cur.
        While cur is not None:
            Create a new node with the same value as the current node and store it in the dictionary hash with the current node as the key.
            Move cur to the next node in the original list.

    Reset the cur pointer to the head of the original linked list.

    Traverse the original linked list again using cur.
        While cur is not None:
            Retrieve the copied node from the hash dictionary using cur as the key and store it in the copy variable.
            Set the next pointer of the copy node to the copied node obtained from the hash dictionary using cur.next as the key.
            Set the random pointer of the copy node to the copied node obtained from the hash dictionary using cur.random as the key.
            Move cur to the next node in the original list.

    Return the copied head node obtained from the hash dictionary using the original head node as the key.

This algorithm first creates a mapping of original nodes to their copied nodes and then iterates through the original list twice to connect 
the next and random pointers of the copied nodes. Finally, it returns the head of the copied linked list."""
