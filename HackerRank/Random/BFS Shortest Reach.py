from collections import deque


def bfs(n, m, edges, s):
    graph = {i: [] for i in range(1, n + 1)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    distances = [-1] * (n + 1)
    distances[s] = 0

    queue = deque([s])
    while queue:
        current = queue.popleft()
        for neighbour in graph[current]:
            if distances[neighbour] == -1:
                distances[neighbour] = distances[current] + 6
                queue.append(neighbour)

    result = [distances[i] for i in range(1, n + 1) if i != s]
    return result
