"""A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to
be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because
the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:
Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.

In this challenge, you must first implement a queue using two stacks. Then process q queries, where each query is one of the following 3 types:
1 x: Enqueue element x into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue."""

if __name__ == "__main__":
    q = int(input())
    stack_in = []
    stack_out = []

    for _ in range(q):
        parts = input().split()
        if parts[0] == "1":
            stack_in.append(int(parts[1]))
        elif parts[0] == "2":
            if not stack_out:
                while stack_in:
                    stack_out.append(stack_in.pop())
            stack_out.pop()
        elif parts[0] == "3":
            if not stack_out:
                while stack_in:
                    stack_out.append(stack_in.pop())
            print(stack_out[-1])
