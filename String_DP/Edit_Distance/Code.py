# ============================================
# EDIT DISTANCE (LEVENSHTEIN DISTANCE)
# ============================================

# Problem:
# Given two strings word1 and word2,
# return the minimum number of operations required to convert word1 to word2.
#
# Allowed operations:
# 1. Insert
# 2. Delete
# 3. Replace


# -------------------------------------------------
# 1️⃣ Pure Recursion (Exponential)
# -------------------------------------------------

class RecursionSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(i, j):
            # If word1 finished → insert remaining of word2
            if i == len(word1):
                return len(word2) - j
            
            # If word2 finished → delete remaining of word1
            if j == len(word2):
                return len(word1) - i
            
            # Characters match
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            # Insert, Delete, Replace
            insert = 1 + dfs(i, j + 1)
            delete = 1 + dfs(i + 1, j)
            replace = 1 + dfs(i + 1, j + 1)
            
            return min(insert, delete, replace)

        return dfs(0, 0)


# -------------------------------------------------
# 2️⃣ Memoization (Top-Down DP)
# -------------------------------------------------

class MemoizationSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                insert = 1 + dfs(i, j + 1)
                delete = 1 + dfs(i + 1, j)
                replace = 1 + dfs(i + 1, j + 1)
                memo[(i, j)] = min(insert, delete, replace)
            
            return memo[(i, j)]

        return dfs(0, 0)


# -------------------------------------------------
# 3️⃣ Tabulation (Bottom-Up DP)
# -------------------------------------------------

class TabulationSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],     # Insert
                        dp[i - 1][j],     # Delete
                        dp[i - 1][j - 1]  # Replace
                    )
        
        return dp[m][n]


# -------------------------------------------------
# 4️⃣ Space Optimized (Using 2 Rows)
# -------------------------------------------------

class SpaceOptimizedSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        prev = list(range(n + 1))
        
        for i in range(1, m + 1):
            curr = [i] + [0] * n
            
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(
                        curr[j - 1],    # Insert
                        prev[j],        # Delete
                        prev[j - 1]     # Replace
                    )
            
            prev = curr
        
        return prev[n]


# -------------------------------------------------
# 5️⃣ Fully Space Optimized (Single Row)
# -------------------------------------------------

class SingleRowSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        dp = list(range(n + 1))
        
        for i in range(1, m + 1):
            prev_diag = dp[0]
            dp[0] = i
            
            for j in range(1, n + 1):
                temp = dp[j]
                
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev_diag
                else:
                    dp[j] = 1 + min(
                        dp[j],        # Delete
                        dp[j - 1],    # Insert
                        prev_diag     # Replace
                    )
                
                prev_diag = temp
        
        return dp[n]
