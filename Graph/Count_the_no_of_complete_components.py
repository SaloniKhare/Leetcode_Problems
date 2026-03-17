# ======================================================
# COUNT THE NUMBER OF COMPLETE COMPONENTS - ALL APPROACHES
# ======================================================

# Problem (LeetCode 2685):
# Given an undirected graph with n nodes (0 to n-1) and edges,
# return the number of complete connected components.
#
# A component is COMPLETE if:
# every pair of nodes in that component has an edge between them.
#
# i.e., for k nodes → edges must be k*(k-1)/2


# ------------------------------------------------------
# 1️⃣ DFS Approach
# ------------------------------------------------------

from collections import defaultdict

class DFSSolution:
    def countCompleteComponents(self, n, edges):

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            stack = [node]
            nodes = 0
            edge_count = 0

            while stack:
                curr = stack.pop()

                if curr in visited:
                    continue

                visited.add(curr)
                nodes += 1
                edge_count += len(graph[curr])

                for nei in graph[curr]:
                    if nei not in visited:
                        stack.append(nei)

            return nodes, edge_count // 2


        complete = 0

        for i in range(n):
            if i not in visited:
                nodes, edges_cnt = dfs(i)

                if edges_cnt == nodes * (nodes - 1) // 2:
                    complete += 1

        return complete


# ------------------------------------------------------
# 2️⃣ BFS Approach
# ------------------------------------------------------

from collections import deque, defaultdict

class BFSSolution:
    def countCompleteComponents(self, n, edges):

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        complete = 0

        for i in range(n):

            if i not in visited:

                queue = deque([i])
                nodes = 0
                edges_cnt = 0

                while queue:

                    curr = queue.popleft()

                    if curr in visited:
                        continue

                    visited.add(curr)
                    nodes += 1
                    edges_cnt += len(graph[curr])

                    for nei in graph[curr]:
                        if nei not in visited:
                            queue.append(nei)

                edges_cnt //= 2

                if edges_cnt == nodes * (nodes - 1) // 2:
                    complete += 1

        return complete


# ------------------------------------------------------
# 3️⃣ Union-Find (Disjoint Set)
# ------------------------------------------------------

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.edge_count = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            self.edge_count[px] += 1
            return

        if self.size[px] < self.size[py]:
            px, py = py, px

        self.parent[py] = px
        self.size[px] += self.size[py]
        self.edge_count[px] += self.edge_count[py] + 1


class UnionFindSolution:
    def countCompleteComponents(self, n, edges):

        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u, v)

        complete = 0

        for i in range(n):
            if uf.find(i) == i:  # root
                nodes = uf.size[i]
                edges_cnt = uf.edge_count[i]

                if edges_cnt == nodes * (nodes - 1) // 2:
                    complete += 1

        return complete

