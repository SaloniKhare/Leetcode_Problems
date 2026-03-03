# ============================================
# IS SUBSEQUENCE - ALL APPROACHES
# ============================================

# Problem:
# Given strings s and t,
# return True if s is a subsequence of t.


# -------------------------------------------------
# 1️⃣ Brute Force (Generate All Subsequences of t)
# -------------------------------------------------
# Not practical. Exponential time.

class BruteForceSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def generate(index, current):
            if index == len(t):
                return current == s
            # Include
            if generate(index + 1, current + t[index]):
                return True
            # Exclude
            if generate(index + 1, current):
                return True
            return False
        
        return generate(0, "")


# -------------------------------------------------
# 2️⃣ Two Pointer (Optimal & Most Asked)
# -------------------------------------------------

class TwoPointerSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer for s

        for char in t:
            if i < len(s) and s[i] == char:
                i += 1

        return i == len(s)


# -------------------------------------------------
# 3️⃣ While Loop Two Pointer
# -------------------------------------------------

class WhileLoopSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


# -------------------------------------------------
# 4️⃣ DP (Longest Common Subsequence Based)
# -------------------------------------------------
# If LCS(s, t) == len(s) → True

class DPSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n] == m


# -------------------------------------------------
# 5️⃣ Recursion
# -------------------------------------------------

class RecursionSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def dfs(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False

            if s[i] == t[j]:
                return dfs(i + 1, j + 1)
            else:
                return dfs(i, j + 1)

        return dfs(0, 0)


# -------------------------------------------------
# 6️⃣ Memoization (Top-Down DP)
# -------------------------------------------------

class MemoizationSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = {}

        def dfs(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == t[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = dfs(i, j + 1)

            return memo[(i, j)]

        return dfs(0, 0)
