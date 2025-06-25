# GFG Minimum cost of ropes
"""Great question, Sahil. The line `heapq.heapify(ropes)` transforms the list `ropes` into a **min-heap**, *in place*.

### 🔧 What is a min-heap?
A **min-heap** is a binary heap where the smallest element is always at the front—i.e., `ropes[0]` will always be the shortest rope.
It allows you to efficiently extract the two smallest ropes for merging.

### 💡 Why use `heapify()`?
Without `heapify`, you'd have to search the list every time for the two smallest elements—costing O(n) per operation. `heapify()` lets us do:
- `heapq.heappop()` → pop the smallest element in O(log n)
- `heapq.heappush()` → insert a new rope in O(log n)

So with `heapq.heapify(ropes)`, you instantly prepare `ropes` for priority queue behavior. The total build time is **O(n)**, and it
unlocks efficient greedy operations.
"""

import heapq


def minCost(ropes):
    heapq.heapify(ropes)
    total_cost = 0

    while len(ropes) > 1:
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        cost = first + second
        total_cost += cost
        heapq.heappush(ropes, cost)

    return total_cost


if __name__ == "__main__":
    print(minCost(ropes=[4, 3, 2, 6]))
