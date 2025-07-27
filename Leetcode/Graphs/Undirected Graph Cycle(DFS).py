"""Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry
edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.
"""


class Solution:
    def dfs(self, node, parent, visited, adj):
        visited[node] = True
        
        for neighbour in adj[node]:
            if not visited[neighbour]:
                if self.dfs(neighbour, node, visited, adj):
                    return True
            elif neighbour != parent:
                return True
            
        return False

    def isCycle(self, V, edges):
        # Build adjacency list from edge list
        adj = [[] for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V
        
        for i in range(V):
            if not visited[i]:
                if self.dfs(i, -1, visited, adj):
                    return True
                
        return False



if __name__ == "__main__":
    obj = Solution()
    print(obj.isCycle(V=4, edges=[[0, 1], [0, 2], [1, 2], [2, 3]]))
