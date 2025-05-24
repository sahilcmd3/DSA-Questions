### Stack

## 1. What a Stack Is?

A **stack** is a linear data structure that follows the **Last-In, First-Out (LIFO)** principle. Think of it like a stack of plates: you add new plates on top (push), and you remove plates also from the top (pop). This order is naturally used in many computing scenarios—from managing function calls (the call stack) to undo operations in text editors.

**Key characteristics of a stack:**

- **LIFO Order:** The last element added is the first one removed.  

- **Operations:**  
  - **Push:** Adds an element to the top of the stack.  
  - **Pop:** Removes the element from the top of the stack.  
  - **Peek/Top:** Returns the top element without removing it.  
  - **isEmpty:** Checks whether the stack is empty.  
  - **Size:** Returns the total number of elements in the stack.

These operations usually have an average time complexity of O(1), making stacks efficient for many common tasks.  


---

## 2. Applications of Stacks

Stacks are used in various scenarios, including:

- **Expression Evaluation:** Converting infix expressions to postfix (Reverse Polish Notation).
- **Backtracking Algorithms:** For navigating and retracing steps (e.g., maze solving).
- **Undo Mechanisms:** In editors, to revert to previous states.
- **Depth-First Search (DFS):** In graph traversal algorithms.
- **Managing Function Calls:** The call stack in programming languages uses the stack data structure.

Understanding these practical uses helps in choosing the right type of implementation for your needs.  


---

## 3. Implementing a Stack in Python

Python offers several ways to implement a stack. Let’s explore the most common implementations:

### A. Using Python’s Built-In List

Python lists are dynamic arrays that can efficiently simulate stacks. The methods used are:

- **`append()`** for push.
- **`pop()`** for pop.

**Example:**

```python
# Using a list to implement a stack
stack = []

# Push elements onto the stack
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushes:", stack)

# Peek at the top-most element
print("Peek:", stack[-1])

# Pop elements from the stack
print("Pop:", stack.pop())
print("Stack after pop:", stack)
```

**Notes:**
- **Advantages:**  
  - Simplicity and built-in functionality.
  - Fast for most common operations.
- **Disadvantages:**  
  - In some cases, memory reallocations can cause occasional performance delays if the list grows very large.

This approach is suitable for many everyday use cases.  


---

### B. Using `collections.deque`

The `deque` (double-ended queue) data structure from Python’s `collections` module offers O(1) time complexity for append and pop operations at both ends. This can be useful if you ever need to extend your stack to support efficient additions/removals at both ends.

**Example:**

```python
from collections import deque

# Create a deque for stack implementation
stack = deque()

# Push elements
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack (deque):", list(stack))

# Peek at the top element (last element)
print("Peek:", stack[-1])

# Pop elements from the stack
print("Pop:", stack.pop())
print("Stack after pop:", list(stack))
```

**Notes:**
- **Advantages:**  
  - Consistent O(1) for operations on both ends.
  - More efficient when you need to perform both stack and queue operations.
- **Disadvantages:**  
  - The interface is slightly different from lists, but still very intuitive.

The `deque` is a robust choice when you have performance-critical stack operations.  


---

### C. Using `queue.LifoQueue`

For multithreading scenarios, Python’s `queue.LifoQueue` provides a thread-safe implementation of stack operations. It uses locks internally to ensure that push and pop operations are safe when accessed from multiple threads.

**Example:**

```python
from queue import LifoQueue

# Create a thread-safe stack
stack = LifoQueue()

# Push elements using put()
stack.put('A')
stack.put('B')
stack.put('C')

# Check the size of the stack
print("Stack size:", stack.qsize())

# Pop elements using get()
print("Pop:", stack.get())
print("Stack size after pop:", stack.qsize())
```

**Notes:**
- **Advantages:**  
  - Thread safety, ensuring that concurrent access won’t corrupt the stack.
- **Disadvantages:**  
  - The overhead of locks can lead to slower performance in single-threaded contexts.

This implementation is ideal when you’re working in a concurrent or multi-threaded environment.  


---

### D. Custom Stack Implementation Using a Linked List

For educational purposes—or if you require a more dynamic memory approach—a linked list can be used to implement a stack. In a linked list, each node points to the next, and the stack operations (push and pop) can be implemented in O(1) time.

**Example:**

```python
# Node class for linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Stack class using a linked list
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top  # New node points to the former top
        self.top = new_node       # Update top to the new node
        self.count += 1

    def pop(self):
        if self.isEmpty():
            return None  # Indicates the stack is empty
        popped_value = self.top.value
        self.top = self.top.next  # Move top pointer down the list
        self.count -= 1
        return popped_value

    def peek(self):
        return self.top.value if self.top is not None else None

    def size(self):
        return self.count

# Example usage:
s = Stack()
s.push("A")
s.push("B")
s.push("C")
print("Current stack size:", s.size())
print("Top element:", s.peek())
print("Pop element:", s.pop())
print("New top after pop:", s.peek())
```

**Notes:**
- **Advantages:**  
  - No fixed limits; grows dynamically with available memory.
  - Constant time operations if pointers are managed correctly.
- **Disadvantages:**  
  - More complex to implement compared to using a built-in list.
  - Typically requires more memory overhead because of the node objects.

This custom approach is excellent for learning how data structures work at a low level.  


---

## 4. Performance Considerations

When choosing an implementation, consider the following:

- **Python List:**  
  - *Best for:* Simplicity and fast operations in most use cases.  
  - *Complexity:* O(1) (amortized) for push/pop.
  
- **`collections.deque`:**  
  - *Best for:* Scenarios needing fast addition/removal from either end.  
  - *Complexity:* O(1) for appending and popping from both ends.
  
- **`queue.LifoQueue`:**  
  - *Best for:* Multithreading scenarios.  
  - *Complexity:* O(1), with thread safety overhead.

- **Linked List Based Stack:**  
  - *Best for:* Educational purposes or when managing memory allocations manually.  
  - *Complexity:* O(1) for push/pop, but with extra memory overhead per element.

Each method is optimal under different scenarios, so your choice depends on your specific requirements and constraints.

---

[GeeksforGeeks](https://www.geeksforgeeks.org/stack-in-python/) and [Real Python’s guide on implementing stacks](https://realpython.com/how-to-implement-python-stack/).  


---


### Monotonic Stack
A monotonic stack is a data structure designed to maintain its elements in either an increasing or decreasing order (hence "monotonic"). It's particularly useful for solving 
problems involving ranges or intervals, such as finding the next greater or smaller elements in an array.

### Monotonic Stack Algorithm
Here’s a general approach to implementing a monotonic stack:

1. Initialize an Empty Stack:
   Start with an empty stack to store elements (or their indices).

2. Traverse the Array:
   Iterate through the elements of the array. For each element:

   - While the stack is not empty and the current element violates the monotonic order with the element at the top of the stack:
     - Perform necessary computations (e.g., calculate a result or update a value).
     - Pop the top element from the stack.
   - Push the current element (or its index) onto the stack.

3. Post-Traversal:
   After the loop, elements left in the stack might represent unresolved cases depending on the problem.

### Key Points
- For an increasing monotonic stack, new elements are added only if they're larger than the top element of the stack.
- For a decreasing monotonic stack, new elements are added only if they're smaller than the top element.

### Example Problem: "Next Greater Element"
You can use a monotonic decreasing stack to solve this. Here's how:
1. Traverse the array from left to right.
2. While the current element is greater than the top element of the stack, pop elements and record the current element as their "next greater".
3. Push the current element onto the stack.

Monotonic stacks are versatile and frequently used in solving algorithmic problems. Here are some common applications:

### 1. Next Greater/Smaller Element Problems
   - Problem: Find the next greater or smaller element for each element in an array.
   - Use: Efficiently solve these problems in ( O(n) ) time.
   - Example: Stock span problem, where you determine the number of consecutive days with the stock price less than or equal to the current day's price.

### 2. Histogram Problems
   - Problem: Find the largest rectangle in a histogram.
   - Use: A monotonic stack helps calculate the largest area efficiently by keeping track of bars in increasing or decreasing order.
   - Example: This approach is often used to find the maximum area in a binary matrix.

### 3. Trapping Rain Water
   - Problem: Calculate how much rainwater can be trapped after a rainfall given the elevation map.
   - Use: Monotonic stacks can determine the boundaries (left and right) of trapped water efficiently.
   - Example: The "Trapping Rain Water" problem on coding platforms like LeetCode.

### 4. Sliding Window Maximum/Minimum
   - Problem: Find the maximum or minimum element in every sliding window of a given size ( k ).
   - Use: Helps maintain the order while efficiently querying window extremes.

### 5. Merging Intervals
   - Problem: Merge overlapping intervals to minimize the number of ranges.
   - Use: Monotonic stacks are often employed for this by sorting intervals and pushing them into the stack based on their boundaries.

### 6. Valid Parentheses
   - Problem: Check whether a given string of parentheses is valid or not.
   - Use: Monotonic stacks are used to match opening and closing brackets efficiently.

### 7. Stock Span
   - Problem: Determine the span of the stock price for each day (how many consecutive days the price was less or equal).
   - Use: Efficiently solve this using a monotonic stack.