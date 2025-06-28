"""Given an undirected, weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by 2d array edges[][], where
edges[i]=[u, v, w] represents the edge between the nodes u and v having w edge weight.
You have to find the shortest distance of all the vertices from the source vertex src, and return an array of integers where the ith
element denotes the shortest distance between ith node and source vertex src.

Note: The Graph is connected and doesn't contain any negative weight edge."""

import heapq


class Solution:
    def dijkstra(self, V, edges, src):
        # Building adjacency list
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # Because the graph is undirected

        # Initializing distance array and min-heap (priority queue)
        dist = [float("inf")] * V
        dist[src] = 0
        heap = [(0, src)]  # (distance, vertex)

        # Main loop using priority queue
        while heap:
            current_dist, u = heapq.heappop(heap)

            for neighbour, weight in adj[u]:
                if current_dist + weight < dist[neighbour]:
                    dist[neighbour] = current_dist + weight
                    heapq.heappush(heap, (dist[neighbour], neighbour))

        return dist


if __name__ == "__main__":
    obj = Solution()
    print(obj.dijkstra(V=3, edges=[[0, 1, 1], [1, 2, 3], [0, 2, 6]], src=2))
