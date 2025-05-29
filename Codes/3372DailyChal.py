# LEETCODE (medium)

"""There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates
that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes
ui and vi in the second tree. You are also given an integer k.

Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target
to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you
have to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next
query."""


from collections import deque


# Time Complexity: O(N1∗(N1+E1)+N2∗(N2+E2))
class Solution:
    def maxTargetNodes(self, edges1, edges2, k):
        def bfs(start, adj, k):
            if k == 0:
                return 1
            visited = set([start])
            q = deque([start])
            level = 0
            nodes_reached = 1

            while q and level < k:
                for _ in range(len(q)):
                    node = q.popleft()
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                            nodes_reached += 1
                level += 1
            return nodes_reached

        n = max(max(e) for e in edges1) + 1
        m = max(max(e) for e in edges2) + 1

        adj1 = [[] for _ in range(n)]
        adj2 = [[] for _ in range(m)]

        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        path1 = [bfs(i, adj1, k) for i in range(n)]

        max_found = 0
        if k > 0:
            for i in range(m):
                max_found = max(max_found, bfs(i, adj2, k - 1))

        return [p + max_found for p in path1]


obj = Solution()
print(
    obj.maxTargetNodes(
        edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
        edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
        k=2,
    )
)


"""Approach:

Parse the Graphs: Construct adjacency lists for both trees from the edge lists. Determine the size of each graph based 
    on the largest node index.

BFS on Tree1: For each node in tree1, perform a BFS up to depth k and count how many nodes can be reached. Store these counts in 
    path1[].

BFS on Tree2: For each node in tree2, perform a BFS up to depth k-1 (since you can teleport into tree2 and then move k-1 steps). 
    Keep track of the maximum count obtained across all nodes.

Combine Results: Add the maximum number of reachable nodes in tree2 to each entry in path1[], representing the best case if 
    teleporting is used optimally.

Return path1: Each value represents the maximum reachable nodes if starting from the corresponding node in tree1."""
