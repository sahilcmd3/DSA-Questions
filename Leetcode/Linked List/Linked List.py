# Linked List creation
# Define the ListNode class to represent a node in a linked list.
class ListNode:
    def __init__(self, x):
        self.val = x       # Initialize the node's value with x.
        self.next = None   # Initialize the next pointer to None, meaning no next node yet.

if __name__ == "__main__":
    # Read the number of elements n from the input.
    n = int(input())
    
    # Initialize an empty list to store the integer values.
    nums = []
    
    # Loop n times to read each integer and append it to the list.
    for _ in range(n):
        x = int(input())   # Read one integer from input.
        nums.append(x)     # Add the integer to the nums list.
        
    # Create a dummy node which serves as a starting point for the linked list.
    # Using a dummy node simplifies list operations (like insertion) as we don't need to check if the list is empty.
    dummy = ListNode(-1)
    
    # 'temp' will be used as an iterator to build the list, starting from the dummy node.
    temp = dummy
    
    # Iterate over each number in the nums list to create linked list nodes.
    for x in nums:
        node = ListNode(x)  # Create a new node with the current value.
        temp.next = node    # Link the current node to the new node.
        temp = node         # Move the pointer to the new node.
    
    # Reset temp to the start of the actual linked list (skipping the dummy node).
    temp = dummy.next
    
    # Traverse the linked list and print each node's value.
    while temp is not None:
        # Print the value followed by a space. 'end=" "' prevents the default newline.
        print(temp.val, end=" ")
        temp = temp.next  # Move to the next node in the list.
