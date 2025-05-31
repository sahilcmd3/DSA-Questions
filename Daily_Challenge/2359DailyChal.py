# LEETCODE (Medium)

"""You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node
i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from
node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest
index, and if no possible answer exists, return -1.

Note that edges may contain cycles."""


class Sol:
    def getDistances(self, edges, start):  # Finds the shortest distance from each node
        n = len(edges)
        dist = [-1] * n
        d = 0

        while start != -1 and dist[start] == -1:
            dist[start] = d
            d += 1
            start = edges[start]

        return dist

    def closestMeetingNode(self, edges, node1, node2):
        dist1 = self.getDistances(edges, node1)
        dist2 = self.getDistances(edges, node2)

        result = -1
        minDistance = float("inf")

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                maxDist = max(dist1[i], dist2[i])
                if maxDist < minDistance:
                    minDistance = maxDist
                    result = i

        return result


obj = Sol()
print(obj.closestMeetingNode(edges=[2, 2, 3, -1], node1=0, node2=1))
