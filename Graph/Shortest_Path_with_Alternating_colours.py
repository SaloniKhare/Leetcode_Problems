# ============================================
# SHORTEST PATH WITH ALTERNATING COLORS
# ============================================

# Problem:
# You are given:
# n nodes labeled 0 to n-1
# redEdges and blueEdges
# Return shortest distance from node 0 to every node
# such that edge colors alternate.


# -------------------------------------------------
# 1️⃣ BFS (Standard Optimal Approach)
# -------------------------------------------------

from collections import defaultdict, deque

class BFSSolution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        graph = defaultdict(list)

        # Build graph with color information
        for u, v in redEdges:
            graph[u].append((v, 'R'))
        for u, v in blueEdges:
            graph[u].append((v, 'B'))

        # dist[node][color]
        dist = [[float('inf')] * 2 for _ in range(n)]
        # 0 -> Red, 1 -> Blue

        queue = deque()

        # Start from node 0 with both color possibilities
        queue.append((0, 0))  # last edge red
        queue.append((0, 1))  # last edge blue
        dist[0][0] = dist[0][1] = 0

        while queue:
            node, color = queue.popleft()

            for neighbor, edgeColor in graph[node]:
                nextColor = 0 if edgeColor == 'R' else 1

                # Alternate color condition
                if nextColor != color and dist[neighbor][nextColor] == float('inf'):
                    dist[neighbor][nextColor] = dist[node][color] + 1
                    queue.append((neighbor, nextColor))

        result = []
        for r, b in dist:
            shortest = min(r, b)
            result.append(-1 if shortest == float('inf') else shortest)

        return result


# -------------------------------------------------
# 2️⃣ BFS Using Visited Set Instead of Dist Matrix
# -------------------------------------------------

class BFSVisitedSolution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        graph = defaultdict(list)

        for u, v in redEdges:
            graph[u].append((v, 0))  # Red
        for u, v in blueEdges:
            graph[u].append((v, 1))  # Blue

        result = [-1] * n
        visited = set()
        queue = deque([(0, 0, -1)])  # node, distance, last_color

        while queue:
            node, dist, last_color = queue.popleft()

            if result[node] == -1:
                result[node] = dist

            for neighbor, color in graph[node]:
                if color != last_color and (neighbor, color) not in visited:
                    visited.add((neighbor, color))
                    queue.append((neighbor, dist + 1, color))

        return result


# -------------------------------------------------
# 3️⃣ DFS + Memoization (Not Optimal for Shortest Path)
# -------------------------------------------------

class DFSMemoSolution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        graph = defaultdict(list)

        for u, v in redEdges:
            graph[u].append((v, 0))
        for u, v in blueEdges:
            graph[u].append((v, 1))

        memo = {}
        result = [float('inf')] * n

        def dfs(node, last_color, length, visited):
            result[node] = min(result[node], length)

            for neighbor, color in graph[node]:
                if color != last_color and (neighbor, color) not in visited:
                    visited.add((neighbor, color))
                    dfs(neighbor, color, length + 1, visited)
                    visited.remove((neighbor, color))

        dfs(0, -1, 0, set())

        return [-1 if x == float('inf') else x for x in result]


# -------------------------------------------------
# 4️⃣ Level Order BFS (Clear Interview Style)
# -------------------------------------------------

class LevelOrderBFSSolution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        graph = defaultdict(list)

        for u, v in redEdges:
            graph[u].append((v, 0))
        for u, v in blueEdges:
            graph[u].append((v, 1))

        dist = [[-1] * 2 for _ in range(n)]
        queue = deque()

        queue.append((0, 0))  # Assume last was red
        queue.append((0, 1))  # Assume last was blue
        dist[0][0] = dist[0][1] = 0

        while queue:
            node, color = queue.popleft()

            for neighbor, edgeColor in graph[node]:
                if edgeColor != color and dist[neighbor][edgeColor] == -1:
                    dist[neighbor][edgeColor] = dist[node][color] + 1
                    queue.append((neighbor, edgeColor))

        result = []
        for r, b in dist:
            if r == -1 and b == -1:
                result.append(-1)
            elif r == -1:
                result.append(b)
            elif b == -1:
                result.append(r)
            else:
                result.append(min(r, b))

        return result
