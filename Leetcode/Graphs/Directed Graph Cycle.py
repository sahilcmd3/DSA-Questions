"""Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from verticex u to v.
"""

from collections import defaultdict


class Solution:
    # DFS function
    def dfs(self, node):
        self.visited[node] = True
        self.recStack[node] = True

        for neighbour in self.adj[node]:
            if not self.visited[neighbour]:
                if self.dfs(neighbour):
                    return True
            elif self.recStack[neighbour]:
                return True

        self.recStack[node] = False

        return False
    
    def isCycle(self, V, edges):
        # Building adjacency list
        self.adj = defaultdict(list)
        for u, v in edges:
            self.adj[u].append(v)

        # Visited and Recursion Stack arrays
        self.visited = [False] * V
        self.recStack = [False] * V

        # Run DFS for each component
        for i in range(V):
            if not self.visited[i]:
                if self.dfs(i):
                    return True
                
        return False


if __name__ == "__main__":
    obj = Solution()
    # Test case with a cycle
    print("Cyclic Graph:", obj.isCycle(V=4, edges=[[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]))

    # Test case without a cycle
    obj2 = Solution()
    print("Acyclic Graph:", obj2.isCycle(V=4, edges=[[0, 1], [0, 2], [1, 2], [2, 3]]))
