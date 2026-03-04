# ============================================
# DISTINCT SUBSEQUENCES - ALL APPROACHES
# ============================================

# Problem:
# Given two strings s and t,
# return the number of distinct subsequences of s
# which equals t.


# -------------------------------------------------
# 1️⃣ Pure Recursion (Exponential)
# -------------------------------------------------

class RecursionSolution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(i, j):
            # If we formed t
            if j == len(t):
                return 1
            
            # If s finished but t not formed
            if i == len(s):
                return 0
            
            if s[i] == t[j]:
                # Take + Skip
                return dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # Only skip
                return dfs(i + 1, j)
        
        return dfs(0, 0)


# -------------------------------------------------
# 2️⃣ Memoization (Top-Down DP)
# -------------------------------------------------

class MemoizationSolution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if s[i] == t[j]:
                memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                memo[(i, j)] = dfs(i + 1, j)
            
            return memo[(i, j)]

        return dfs(0, 0)


# -------------------------------------------------
# 3️⃣ Tabulation (Bottom-Up DP)
# -------------------------------------------------

class TabulationSolution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # If t is empty → 1 way
        for i in range(m + 1):
            dp[i][0] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]


# -------------------------------------------------
# 4️⃣ Space Optimized (2 Rows)
# -------------------------------------------------

class SpaceOptimizedSolution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        prev = [0] * (n + 1)
        prev[0] = 1
        
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            curr[0] = 1
            
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]
            
            prev = curr
        
        return prev[n]


# -------------------------------------------------
# 5️⃣ Fully Space Optimized (1D DP - Most Important)
# -------------------------------------------------

class SingleRowSolution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, m + 1):
            # Traverse backwards to avoid overwriting
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        
        return dp[n]
