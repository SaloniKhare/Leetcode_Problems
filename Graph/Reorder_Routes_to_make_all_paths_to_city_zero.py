# ============================================================
# REORDER ROUTES TO MAKE ALL PATHS LEAD TO CITY ZERO
# ============================================================

# Problem:
# n cities numbered 0 → n-1
# connections[i] = [a, b] meaning road goes from a → b
#
# You can reverse any road.
# Return minimum number of edges to reverse so every city
# can reach city 0.


# ------------------------------------------------------------
# 1️⃣ DFS (Graph + Direction Tracking)  ⭐ Most Standard
# ------------------------------------------------------------

from collections import defaultdict

class DFSSolution:
    def minReorder(self, n: int, connections):
        graph = defaultdict(list)

        # Build graph
        for a, b in connections:
            graph[a].append((b, 1))  # original direction
            graph[b].append((a, 0))  # reverse edge (no cost)

        visited = set()

        def dfs(node):
            visited.add(node)
            changes = 0

            for nei, cost in graph[node]:
                if nei not in visited:
                    changes += cost + dfs(nei)

            return changes

        return dfs(0)


# ------------------------------------------------------------
# 2️⃣ BFS Approach
# ------------------------------------------------------------

from collections import deque

class BFSSolution:
    def minReorder(self, n: int, connections):
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = set([0])
        queue = deque([0])
        changes = 0

        while queue:
            node = queue.popleft()

            for nei, cost in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    changes += cost
                    queue.append(nei)

        return changes


# ------------------------------------------------------------
# 3️⃣ DFS Iterative (Stack)
# ------------------------------------------------------------

class DFSIterativeSolution:
    def minReorder(self, n: int, connections):
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        stack = [0]
        visited = set([0])
        changes = 0

        while stack:
            node = stack.pop()

            for nei, cost in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    changes += cost
                    stack.append(nei)

        return changes


# ------------------------------------------------------------
# 4️⃣ Simple Edge Direction Check (Using Set)
# ------------------------------------------------------------

class EdgeSetSolution:
    def minReorder(self, n: int, connections):
        graph = defaultdict(list)
        edges = set()

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            edges.add((a, b))

        visited = set([0])
        stack = [0]
        changes = 0

        while stack:
            node = stack.pop()

            for nei in graph[node]:
                if nei not in visited:
                    if (node, nei) in edges:
                        changes += 1
                    visited.add(nei)
                    stack.append(nei)

        return changes
