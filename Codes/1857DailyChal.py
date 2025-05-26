# LEETCODE (Hard)

"""There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in
this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed
edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to
xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring
color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
"""


from collections import deque


# Time Complexity: O(N+Edges)
def largestValue(colors, edges):
    n = len(colors)
    adj = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    dp = [[0] * 26 for _ in range(n)]
    queue = deque()

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
        dp[i][ord(colors[i]) - ord("a")] = 1

    visited = 0
    maxColor = 0

    while queue:
        node = queue.popleft()
        visited += 1

        for neighbour in adj[node]:
            for c in range(26):
                inc = 1 if ord(colors[neighbour]) - ord("a") == c else 0
                dp[neighbour][c] = max(dp[neighbour][c], dp[node][c] + inc)

            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

        maxColor = max(maxColor, max(dp[node]))

    return maxColor if visited == n else -1


print(largestValue(colors="a", edges=[[0, 0]]))
