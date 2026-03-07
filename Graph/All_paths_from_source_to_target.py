# ============================================================
# ALL PATHS FROM SOURCE TO TARGET (DAG)
# ============================================================

# Problem:
# Given a DAG graph represented as adjacency list:
# graph[i] = list of nodes you can visit from i
#
# Return all possible paths from node 0 → node n-1


# ------------------------------------------------------------
# 1️⃣ DFS + Backtracking (Most Standard)
# ------------------------------------------------------------

class DFSBacktrackingSolution:
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        result = []
        path = [0]

        def dfs(node):
            if node == target:
                result.append(path[:])
                return

            for nei in graph[node]:
                path.append(nei)
                dfs(nei)
                path.pop()

        dfs(0)
        return result


# ------------------------------------------------------------
# 2️⃣ DFS Simple (Passing Path)
# ------------------------------------------------------------

class DFSSimpleSolution:
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        result = []

        def dfs(node, path):
            if node == target:
                result.append(path)
                return

            for nei in graph[node]:
                dfs(nei, path + [nei])

        dfs(0, [0])
        return result


# ------------------------------------------------------------
# 3️⃣ BFS Approach
# ------------------------------------------------------------

from collections import deque

class BFSSolution:
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        queue = deque([[0]])
        result = []

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == target:
                result.append(path)
                continue

            for nei in graph[node]:
                queue.append(path + [nei])

        return result


# ------------------------------------------------------------
# 4️⃣ DFS + Memoization
# ------------------------------------------------------------

class DFSMemoSolution:
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        memo = {}

        def dfs(node):
            if node == target:
                return [[target]]

            if node in memo:
                return memo[node]

            paths = []

            for nei in graph[node]:
                for path in dfs(nei):
                    paths.append([node] + path)

            memo[node] = paths
            return paths

        return dfs(0)


# ------------------------------------------------------------
# 5️⃣ Iterative DFS (Stack)
# ------------------------------------------------------------

class DFSIterativeSolution:
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        stack = [(0, [0])]
        result = []

        while stack:
            node, path = stack.pop()

            if node == target:
                result.append(path)
                continue

            for nei in graph[node]:
                stack.append((nei, path + [nei]))

        return result
