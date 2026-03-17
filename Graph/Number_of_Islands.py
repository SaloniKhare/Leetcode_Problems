# ======================================================
# NUMBER OF ISLANDS - ALL APPROACHES
# ======================================================

# Problem (LeetCode 200):
# Given a 2D grid of '1's (land) and '0's (water),
# count the number of islands.
# An island is surrounded by water and is formed by
# connecting adjacent lands horizontally or vertically.


# ------------------------------------------------------
# 1️⃣ DFS (Recursive)
# ------------------------------------------------------

class DFSSolution:
    def numIslands(self, grid):

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):

            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            grid[r][c] = '0'  # mark visited

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count


# ------------------------------------------------------
# 2️⃣ BFS (Queue)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def numIslands(self, grid):

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == '1':
                    count += 1

                    queue = deque([(r, c)])
                    grid[r][c] = '0'

                    while queue:
                        x, y = queue.popleft()

                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy

                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                queue.append((nx, ny))

        return count


# ------------------------------------------------------
# 3️⃣ Union-Find (Disjoint Set)
# ------------------------------------------------------

class UnionFind:
    def __init__(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        self.parent = {}
        self.rank = {}
        self.count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.parent[(r,c)] = (r,c)
                    self.rank[(r,c)] = 0
                    self.count += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

            self.count -= 1


class UnionFindSolution:
    def numIslands(self, grid):

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        uf = UnionFind(grid)

        directions = [(1,0), (0,1)]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == '1':
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy

                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            uf.union((r,c), (nr,nc))

        return uf.count

ow in grid]))
