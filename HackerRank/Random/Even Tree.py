"""a tree — a connected graph with no cycles — consisting of nodes connected by edges. The task is to remove as many edges
as possible so that the resulting forest (i.e., group of disconnected subtrees) has only components with an even number of nodes.
"""

from collections import defaultdict


def evenForest(t_nodes, t_edges, t_from, t_to):
    # Build the adjacency list
    graph = defaultdict(list)
    for u, v in zip(t_from, t_to):
        graph[u].append(v)
        graph[v].append(u)

    removable_edges = 0

    def dfs(node, parent):
        nonlocal removable_edges
        subtree_size = 1  # count current node

        for neighbor in graph[node]:
            if neighbor != parent:
                size = dfs(neighbor, node)
                if size % 2 == 0:
                    removable_edges += 1
                else:
                    subtree_size += size

        return subtree_size

    dfs(1, 0)  # start DFS from node 1 with no parent

    return removable_edges
