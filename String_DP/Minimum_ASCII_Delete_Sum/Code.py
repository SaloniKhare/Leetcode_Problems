# =========================================================
# MINIMUM ASCII DELETE SUM FOR TWO STRINGS - ALL APPROACHES
# =========================================================

# Problem:
# Given two strings s1 and s2,
# return the minimum sum of ASCII values of characters
# you need to delete to make the two strings equal.


# ---------------------------------------------------------
# 1️⃣ Pure Recursion (Exponential)
# ---------------------------------------------------------

class RecursionSolution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def dfs(i, j):
            if i == len(s1):
                return sum(ord(c) for c in s2[j:])
            if j == len(s2):
                return sum(ord(c) for c in s1[i:])
            
            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1)
            
            delete_s1 = ord(s1[i]) + dfs(i + 1, j)
            delete_s2 = ord(s2[j]) + dfs(i, j + 1)
            
            return min(delete_s1, delete_s2)
        
        return dfs(0, 0)


# ---------------------------------------------------------
# 2️⃣ Memoization (Top-Down DP)
# ---------------------------------------------------------

class MemoizationSolution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}

        def dfs(i, j):
            if i == len(s1):
                return sum(ord(c) for c in s2[j:])
            if j == len(s2):
                return sum(ord(c) for c in s1[i:])
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if s1[i] == s2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                delete_s1 = ord(s1[i]) + dfs(i + 1, j)
                delete_s2 = ord(s2[j]) + dfs(i, j + 1)
                memo[(i, j)] = min(delete_s1, delete_s2)
            
            return memo[(i, j)]

        return dfs(0, 0)


# ---------------------------------------------------------
# 3️⃣ Tabulation (Bottom-Up DP)
# ---------------------------------------------------------

class TabulationSolution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases
        for i in range(m - 1, -1, -1):
            dp[i][n] = dp[i + 1][n] + ord(s1[i])
        
        for j in range(n - 1, -1, -1):
            dp[m][j] = dp[m][j + 1] + ord(s2[j])
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        ord(s1[i]) + dp[i + 1][j],
                        ord(s2[j]) + dp[i][j + 1]
                    )
        
        return dp[0][0]


# ---------------------------------------------------------
# 4️⃣ Space Optimized (2 Rows)
# ---------------------------------------------------------

class SpaceOptimizedSolution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        prev = [0] * (n + 1)
        
        for j in range(n - 1, -1, -1):
            prev[j] = prev[j + 1] + ord(s2[j])
        
        for i in range(m - 1, -1, -1):
            curr = [0] * (n + 1)
            curr[n] = prev[n] + ord(s1[i])
            
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    curr[j] = prev[j + 1]
                else:
                    curr[j] = min(
                        ord(s1[i]) + prev[j],
                        ord(s2[j]) + curr[j + 1]
                    )
            
            prev = curr
        
        return prev[0]


# ---------------------------------------------------------
# 5️⃣ LCS-Based Approach (ASCII Weighted LCS)
# ---------------------------------------------------------
# Idea:
# total_ascii = sum(s1) + sum(s2)
# Find maximum ASCII sum of common subsequence
# Answer = total_ascii - 2 * lcs_ascii

class LCSSolution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        total = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        return total - 2 * dp[m][n]
