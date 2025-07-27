"""class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.print_stack()"""


# Stack using one queue one variable (TC: O(N) and SC: O(N+1) ~ O(N)
# for SC: O(N) pop krke elements ko waapis ussi mein push krdena
from collections import deque


class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        temp = x  # Temporary variable  
        self.q.append(temp)

        # Rotate the queue to maintain LIFO order
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if not self.q:
            return "Stack is empty"
        return self.q.popleft()

    def top(self):
        if not self.q:
            return "Stack is empty"
        return self.q[0]

    def is_empty(self):
        return not self.q


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.top())