# ======================================================
# NEAREST EXIT FROM ENTRANCE IN MAZE - ALL APPROACHES
# ======================================================

# Problem:
# maze -> grid with '.' (empty) and '+' (wall)
# entrance -> [row, col]
# Find the minimum steps to reach the nearest exit.
# Exit = boundary cell (not the entrance).


# ------------------------------------------------------
# 1️⃣ BFS (Optimal Solution) ⭐
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        q = deque()

        q.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = '+'

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, steps = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    
                    # check if exit
                    if nr == 0 or nc == 0 or nr == m-1 or nc == n-1:
                        return steps + 1

                    maze[nr][nc] = '+'
                    q.append((nr, nc, steps + 1))

        return -1


# ------------------------------------------------------
# 2️⃣ BFS with Visited Matrix
# ------------------------------------------------------

class BFSVisitedSolution:
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        visited = [[False]*n for _ in range(m)]

        q = deque()
        q.append((entrance[0], entrance[1], 0))
        visited[entrance[0]][entrance[1]] = True

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, steps = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n and
                    not visited[nr][nc] and maze[nr][nc] == '.'):

                    if nr == 0 or nc == 0 or nr == m-1 or nc == n-1:
                        return steps + 1

                    visited[nr][nc] = True
                    q.append((nr, nc, steps + 1))

        return -1
