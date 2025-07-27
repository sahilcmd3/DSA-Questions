"""If the city map shows main roads, then village roads exist only between pairs of nodes that don't have a main road. So you 
construct the full graph and subtract the existing edges to infer the village roads."""


from collections import deque, defaultdict


def rustMurderer(n, roads, s):
    # Build graph of known roads
    graph = defaultdict(set)
    for u, v in roads:
        graph[u].add(v)
        graph[v].add(u)

    visited = [False] * (n + 1)
    dist = [-1] * (n + 1)
    queue = deque([s])
    visited[s] = True
    dist[s] = 0

    # Track unvisited nodes for fast complement lookup
    not_visited = set(range(1, n + 1))
    not_visited.remove(s)

    while queue:
        current = queue.popleft()
        # Potential neighbors are unvisited and not connected to current
        candidates = not_visited - graph[current]

        for neighbor in candidates:
            visited[neighbor] = True
            dist[neighbor] = dist[current] + 1
            queue.append(neighbor)

        # Remove visited candidates in bulk
        not_visited -= candidates

    return [dist[i] for i in range(1, n + 1) if i != s]


if __name__ == "__main__":
    print(rustMurderer(n=4, roads=[(1, 2), (2, 3), (1, 4)], s=1))
