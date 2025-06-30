import os
def kruskals(g_nodes, g_from, g_to, g_weight):
    # Create edge list: (weight, u, v)
    edges = list(zip(g_weight, g_from, g_to))
    edges.sort()  # Sort by weight, then by u+v+weight if needed

    parent = list(range(g_nodes + 1))
    rank = [0] * (g_nodes + 1)

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u == root_v:
            return False
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            if rank[root_u] == rank[root_v]:
                rank[root_u] += 1
        return True

    mst_weight = 0
    for weight, u, v in edges:
        if union(u, v):
            mst_weight += weight

    return mst_weight


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())
    g_from = []
    g_to = []
    g_weight = []

    for _ in range(g_edges):
        u, v, w = map(int, input().rstrip().split())
        g_from.append(u)
        g_to.append(v)
        g_weight.append(w)

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    fptr.write(str(res) + '\n')
    fptr.close()
