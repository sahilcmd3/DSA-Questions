# LEETCODE

"""You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed
edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal
to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is
impossible for all the n nodes to receive the signal, return -1."""


"""How it works:
Builds a directed graph from the input.
Uses a min-heap to always expand the node with the smallest known distance.
Updates distances to neighbors if a shorter path is found.
Returns the maximum distance from the source to any node (i.e., the time it takes for the signal to reach the farthest node)."""


import heapq
from typing import List


class Solution:
    @staticmethod
    def networkDelayTime(times, n, k):
        # Build the graph as an adjacency list
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        # Distance and priority queue
        dist = {i: float("inf") for i in range(1, n + 1)}
        dist[k] = 0
        min_heap = [(0, k)]  # Distance and node

        # Dijkstra
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if time > dist[node]:
                continue
            for neighbour, weight in graph[node]:
                if dist[neighbour] > time + weight:
                    dist[neighbour] = time + weight
                    heapq.heappush(min_heap, (dist[neighbour], neighbour))

        # Maximum time to reach any node
        max_time = max(dist.values())

        return max_time if max_time < float("inf") else -1


if __name__ == "__main__":
    obj = Solution()
    print(obj.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
