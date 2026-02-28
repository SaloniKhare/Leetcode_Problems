# Find eventual safe states 
""" There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order."""
class Solution:
    def dfs(self, adj, src, vis, recst):
        vis[src] = True
        recst[src] = True
        for x in adj[src]:
            if not vis[x] and self.dfs(adj, x, vis, recst):
                return True
            elif recst[x]:
                return True
        recst[src] = False
        return False

    def eventualSafeNodes(self, graph):
        n = len(graph)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(len(graph[i])):
                adj[i].append(graph[i][j])

        vis = [False] * n
        recst = [False] * n
        for i in range(n):
            if not vis[i]:
                self.dfs(adj, i, vis, recst)

        ans = []
        for i in range(len(recst)):
            if not recst[i]:
                ans.append(i)
        return ans
