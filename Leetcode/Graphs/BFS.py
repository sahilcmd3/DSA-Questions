"""Given a connected undirected graph containing V vertices, represented by a 2-d adjacency list adj[][], where each adj[i]
represents the list of vertices connected to vertex i. Perform a Breadth First Search (BFS) traversal starting from vertex 0,
visiting vertices from left to right according to the given adjacency list, and return a list containing the BFS traversal of the graph.

Note: Do traverse in the same order as they are in the given adjacency list."""

from collections import deque


class Solution:
    def bfs(self, adj):
        V = len(adj)
        visited = [False] * V
        result = []
        queue = deque()

        # start bfs from node 0
        visited[0] = True
        queue.append(0)

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbour in adj[node]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True

        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.bfs(adj=[[2, 3, 1], [0], [0, 4], [0], [2]]))



"""Badhia, let's break it down line-by-line in simple Hinglish to make sure the **BFS of Graph** code using class format becomes crystal clear:

```python
from collections import deque
```
- `deque` ek fast queue hai jo hum BFS ke liye use karenge. Isse left se pop and right se append dono efficient hota hai.

```python
class Solution:
```
- Ek class define ki gayi jiska naam `Solution` hai—GeeksforGeeks aise format me code mangta hai.

```python
    def bfsOfGraph(self, V, adj):
```
- Ye method BFS traversal return karega.  
• `V` → total number of vertices  
• `adj` → adjacency list (har node ke neighbors ka list)

```python
        visited = [False] * V
```
- Ek `visited` list banayi jisme har vertex initially `False` hai—matlab kisi node ko abhi tak visit nahi kiya gaya.

```python
        result = []
```
- BFS traversal ka result store karne ke liye ek empty list.

```python
        queue = deque()
```
- BFS ke liye queue chahiye hoti hai—so yahan ek `deque` banayi.

```python
        visited[0] = True
        queue.append(0)
```
- Hum graph traversal **hamesha node 0 se start** karte hain.  
• Pehle 0 ko visited mark kiya  
• Aur queue me daal diya processing ke liye

```python
        while queue:
```
- Jab tak queue empty nahi ho jati, hum BFS chalayenge—ye loop BFS ka core hai.

```python
            node = queue.popleft()
```
- Queue ke front se ek node nikalo (FIFO style) — is node ko ab visit karne ka time hai.

```python
            result.append(node)
```
- Jo node abhi nikala, usko `result` me add kar do.

```python
            for neighbor in adj[node]:
```
- Ab us node ke sab neighbors check karo—jo adjacency list me diye gaye hain.

```python
                if not visited[neighbor]:
```
- Agar koi neighbor abhi tak visit nahi hua…

```python
                    visited[neighbor] = True
                    queue.append(neighbor)
```
- …to usko visited mark karo aur queue me daal do taaki future me process ho.

```python
        return result
```
- Jab sab nodes explore ho jayein, final `result` return karo jisme BFS ka order hoga.
"""
