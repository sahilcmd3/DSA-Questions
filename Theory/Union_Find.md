A disjoint set is a collection of sets where no two sets share any common elements. In other words, the intersection of any two sets in the
collection is empty.

### Example of Disjoint Sets
Consider these two sets:
- Set A = {1, 2, 3}
- Set B = {4, 5, 6}

Since A ∩ B = ∅ (no common elements), they are disjoint.

### Mathematical Definition
Two sets A and B are disjoint if:
[A cap B = emptyset]
This means that their intersection is the empty set.

### Applications of Disjoint Sets
- Graph Algorithms (e.g., Kruskal’s Algorithm for Minimum Spanning Tree)
- Dynamic Connectivity Problems
- Union-Find Data Structure (used for efficiently managing disjoint sets)

[BYJU'S](https://byjus.com/maths/disjoint-set/)


Union-Find, also known as Disjoint Set Union (DSU), is a data structure used to efficiently manage and merge disjoint sets. It is particularly
useful in problems involving connectivity, such as graph algorithms and network clustering.

### Core Operations
Union-Find supports two main operations:
1. Find (`find_set(v)`) – Determines which set an element belongs to.
2. Union (`union_sets(a, b)`) – Merges two sets into one.

### How It Works
- Each element starts in its own set.
- The Find operation helps identify the "leader" or "representative" of a set.
- The Union operation merges two sets by linking their representatives.

### Optimizations
To make Union-Find efficient, we use:
1. Path Compression – Flattens the structure to speed up future lookups.
2. Union by Rank – Ensures smaller trees are merged under larger ones to keep the structure balanced.

### Example Implementation
```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
```

### Use Cases
- Connected Components in Graphs
- Cycle Detection in Graphs
- Kruskal’s Algorithm for Minimum Spanning Tree
- Dynamic Connectivity Problems

(https://www.tutorialspoint.com/introduction-to-disjoint-set-data-structure-or-union-find-algorithm)