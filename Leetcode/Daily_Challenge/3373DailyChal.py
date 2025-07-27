# LEETCODE (Hard)
# VISIT AGAIN

"""There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi]
indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an
edge between nodes ui and vi in the second tree.

Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the
first tree if you had to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to
the next query."""


class Test:
    def dfs(self, node, color, graph, component, bipartite):
        # Purpose: Performs bipartite coloring of the tree
        #   bipartite[color] += 1: Counts nodes in each color group
        #   component[node] = color: Assigns color (0 or 1) to current node
        #   1 - color: Alternates between colors 0 and 1 for neighbors
        #   Key insight: In a tree, nodes at even distances get same color, odd distances get different color

        bipartite[color] += 1
        component[node] = color

        for neighbour in graph[node]:
            if component[neighbour] == -1:
                self.dfs(neighbour, 1 - color, graph, component, bipartite)

    def build_graph(self, edges, n):
        # Purpose: Converts edge list to adjacency list representation
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        return graph

    def maxTargetNodes(self, edges1, edges2):
        # Algorithm Logic
        #   Bipartite Coloring: Each tree is colored with alternating colors (0,1). Nodes with same color are at even distances from each other.
        #   Tree1 Analysis: For each node, count how many nodes in tree1 are at even distances (same color).
        #   Tree2 Analysis: Find the larger of the two color groups in tree2.
        #   Optimal Connection: When connecting trees, we can choose any node from tree2's larger group to maximize targets.
        #   Final Answer: For each node in tree1, the maximum targets = (same-color nodes in tree1) + (larger color group in tree2).

        n1, n2 = len(edges1) + 1, len(edges2) + 1

        graph1 = self.build_graph(edges1, n1)
        graph2 = self.build_graph(edges2, n2)

        component1 = [-1] * n1
        bipartite1 = [0, 0]
        self.dfs(0, 0, graph1, component1, bipartite1)

        ans = [bipartite1[component1[i]] for i in range(n1)]

        component2 = [-1] * n2
        bipartite2 = [0, 0]
        self.dfs(0, 0, graph2, component2, bipartite2)

        max_bipartite2 = max(bipartite2)

        return [val + max_bipartite2 for val in ans]


obj = Test()
print(
    obj.maxTargetNodes(
        edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
        edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
    )
)
