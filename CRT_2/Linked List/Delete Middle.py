# LEETCODE 2095

class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
        

def deleteMiddle(head):
    if not head or not head.next:
        return None
    
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
        
    mid = count // 2
    temp = head
    for _ in range(mid - 1):
        temp = temp.next
    
    temp.next = temp.next.next
    
    return head
