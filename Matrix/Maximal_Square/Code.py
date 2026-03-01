# ==============================
# MAXIMAL SQUARE - ALL APPROACHES
# ==============================

# Problem:
# Given an m x n binary matrix filled with 0's and 1's,
# find the largest square containing only 1's and return its area.


# -------------------------------------------------
# 1️⃣ Recursion
# -------------------------------------------------
class RecursionSolution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.max_side = 0
        def helper(i, j):
            if i >= m or j >= n:
                return 0
            down = helper(i + 1, j)
            right = helper(i, j + 1)
            diag = helper(i + 1, j + 1)

            if matrix[i][j] == '1':
                side = 1 + min(down, right, diag)
                self.max_side = max(self.max_side, side)
                return side
            else:
                return 0
        helper(0, 0)
        return self.max_side ** 2


# -------------------------------------------------
# 2️⃣ Memoization
# -------------------------------------------------
class MemoizationSolution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        memo = {}
        self.max_side = 0
        def helper(i, j):
            if i >= m or j >= n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            down = helper(i + 1, j)
            right = helper(i, j + 1)
            diag = helper(i + 1, j + 1)
            if matrix[i][j] == '1':
                side = 1 + min(down, right, diag)
                self.max_side = max(self.max_side, side)
                memo[(i, j)] = side
            else:
                memo[(i, j)] = 0
            return memo[(i, j)]
        helper(0, 0)
        return self.max_side ** 2


# -------------------------------------------------
# 3️⃣ Tabulation
# -------------------------------------------------
class TabulationSolution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_side = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )
                    max_side = max(max_side, dp[i][j])
        return max_side ** 2


# -------------------------------------------------
# 4️⃣ Space Optimized
# -------------------------------------------------
class SpaceOptimizedSolution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        prev = [0] * (n + 1)
        max_side = 0
        for i in range(1, m + 1):
            current = [0] * (n + 1)
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    current[j] = 1 + min(prev[j], current[j - 1], prev[j - 1])
                    max_side = max(max_side, current[j])
            prev = current

        return max_side ** 2
