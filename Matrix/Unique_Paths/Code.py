``` python
# ==============================
# UNIQUE PATHS - ALL APPROACHES
# ==============================

# Problem:
# A robot is located at the top-left corner of a m x n grid.
# The robot can only move either down or right at any point in time.
# Return the number of possible unique paths to reach the bottom-right corner.


class RecursionSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i, j):
            # If out of bounds
            if i >= m or j >= n:
                return 0
            # If reached destination
            if i == m - 1 and j == n - 1:
                return 1
            # Move right + Move down
            return helper(i, j + 1) + helper(i + 1, j)
        return helper(0, 0)


class MemoizationSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def helper(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = helper(i, j + 1) + helper(i + 1, j)
            return memo[(i, j)
        return helper(0, 0)


class TabulationSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


class SpaceOptimizedSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [1] * n
        for i in range(1, m):
            current_row = [1] * n
            for j in range(1, n):
                current_row[j] = current_row[j - 1] + prev_row[j]
            prev_row = current_row
        return prev_row[n - 1]



```
