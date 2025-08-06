# Convert Binary Number in a Linked List to Integer

"""Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
The most significant bit is at the head of the linked list."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity: O(n)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0

        while head:
            num = (num << 1) | head.val
            head = head.next

        return num


if __name__ == "__main__":
    # Helper function to convert list to linked list
    def list_to_linkedlist(lst):
        dummy = ListNode(0)
        curr = dummy

        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
            
        return dummy.next

    # Convert input list to linked list
    input_list = [1, 0, 1]
    head = list_to_linkedlist(input_list)

    obj = Solution()
    print(obj.getDecimalValue(head))
