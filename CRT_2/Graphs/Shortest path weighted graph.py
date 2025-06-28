"""You are given a weighted undirected graph having n vertices numbered from 1 to n and m edges along with their weights. Find the
shortest weight path between the vertex 1 and the vertex n,  if there exists a path, and return a list of integers whose first element
is the weight of the path, and the rest consist of the nodes on that path. If no path exists, then return a list containing a single element -1.

The input list of edges is as follows - {a, b, w}, denoting there is an edge between a and b, and w is the weight of that edge.

Note: The driver code here will first check if the weight of the path returned is equal to the sum of the weights along the nodes on that
path, if equal it will output the weight of the path, else -2. In case the list contains only a single element (-1) it will simply output -1.
"""

import heapq


class Solution:
    @staticmethod
    def shortestPath(n, m, edges):
        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Distance array, parent array for path reconstruction
        dist = [float("inf")] * (n + 1)
        parent = [i for i in range(n + 1)]

        dist[1] = 0
        min_heap = [(0, 1)]  # (dist, node)

        while min_heap:
            d, node = heapq.heappop(min_heap)
            for neighbor, weight in adj[node]:
                if d + weight < dist[neighbor]:
                    dist[neighbor] = d + weight
                    parent[neighbor] = node
                    heapq.heappush(min_heap, (dist[neighbor], neighbor))

        # No path found
        if dist[n] == float("inf"):
            return [-1]

        # Reconstruct path from parent array
        path = []
        curr = n
        while parent[curr] != curr:
            path.append(curr)
            curr = parent[curr]
        path.append(1)
        path.reverse()

        return dist[n]


if __name__ == "__main__":
    obj = Solution()
    print(
        obj.shortestPath(
            n=5,
            m=6,
            edges=[[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]],
        )
    )
