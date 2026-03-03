# ==============================
# KEYS AND ROOMS - ALL APPROACHES
# ==============================

# Problem:
# There are n rooms labeled from 0 to n-1.
# Each room contains keys to other rooms.
# Initially, you can enter room 0.
# Return True if you can visit all rooms.


# -------------------------------------------------
# 1️⃣ DFS - Recursive
# -------------------------------------------------

class DFSRecursiveSolution:
    def canVisitAllRooms(self, rooms):
        visited = set()

        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)
        return len(visited) == len(rooms)


# -------------------------------------------------
# 2️⃣ DFS - Iterative (Stack)
# -------------------------------------------------

class DFSIterativeSolution:
    def canVisitAllRooms(self, rooms):
        visited = set()
        stack = [0]

        while stack:
            room = stack.pop()
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    stack.append(key)

        return len(visited) == len(rooms)


# -------------------------------------------------
# 3️⃣ BFS - Queue
# -------------------------------------------------

from collections import deque

class BFSSolution:
    def canVisitAllRooms(self, rooms):
        visited = set([0])
        queue = deque([0])

        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        return len(visited) == len(rooms)


# -------------------------------------------------
# 4️⃣ Using Boolean Visited Array
# -------------------------------------------------

class BooleanVisitedSolution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False] * n

        def dfs(room):
            visited[room] = True
            for key in rooms[room]:
                if not visited[key]:
                    dfs(key)

        dfs(0)
        return all(visited)


