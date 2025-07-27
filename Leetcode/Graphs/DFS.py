"""Given a connected undirected graph containing V vertices represented by a 2-d adjacency list adj[][], where each adj[i]
represents the list of vertices connected to vertex i. Perform a Depth First Search (DFS) traversal starting from vertex 0, v
isiting vertices from left to right as per the given adjacency list, and return a list containing the DFS traversal of the graph.

Note: Do traverse in the same order as they are in the given adjacency list."""


class Solution:
    def __init__(self):
        self.visited = []
        self.result = []

    def dfsOfGraph(self, v, adj):
        self.visited[v] = True
        self.result.append(v)

        for neighbour in adj[v]:
            if not self.visited[neighbour]:
                self.dfsOfGraph(neighbour, adj)

    def dfs(self, adj):
        V = len(adj)
        self.visited = [False] * V
        self.result = []
        self.dfsOfGraph(0, adj)

        return self.result


if __name__ == "__main__":
    obj = Solution()
    print(obj.dfs(adj=[[2, 3, 1], [0], [0, 4], [0], [2]]))



"""
class Solution:
Yahan hum ek `Solution` naam ki class define kar rahe hain, jisme DFS ka sara logic rahega.

- def __init__(self):
    self.visited = []
    self.result = []
    
**Constructor**: jab bhi `Solution()` object banta hai, yeh run hota hai.  
    • `self.visited = []` → baad mein vertices ka visit-status store karne ke liye list.  
    • `self.result = []`  → DFS ke output order ko collect karne ke liye list. 


- def dfsOfGraph(self, v, adj):

Yeh **recursive helper method** hai jo actually DFS “visit” karta hai.  
  • `v` → current node jisko hum visit karne jaa rahe hain.  
  • `adj` → adjacency-list of the graph.


- self.visited[v] = True

Jab hum `v` pe pahunchte hain, usko “visited” mark karte hain, taaki future mein wapas na jaaye.

- self.result.append(v)

`v` ko `result` list mein add kar diya—yeh hai DFS traversal ka next step.


- for neighbour in adj[v]:

`adj[v]` se milte hain sab connected neighbours of `v`. Har ek pe loop chalega.


- if not self.visited[neighbour]:

Check karo ki woh neighbour pehle visit hua ya nahi.


- self.dfsOfGraph(neighbour, adj)

Agar unvisited hai, to recursive call karke wahan “go deep” kar do.


- def dfs(self, adj):

Yeh woh method hai jo GfG platform call karta—problem signature ke hisaab se sirf `adj` parameter milta.


- V = len(adj)

`V` calculate kiya as number of vertices (adjacency-list ki length ke barabar).


- self.visited = [False] * V

`visited` list ko reset karke size-V boolean list banaya, sab pehle `False`.


- self.result = []

`result` ko bhi fresh empty list se reset kiya.


- self.dfsOfGraph(0, adj)

DFS **start** kiya node `0` se—GfG problem ke rules ke mutabik.


- return self.result

Jab recursion complete ho jaye, to `result` list return ho jati hai, jisme DFS ka final order hota hai.
"""
