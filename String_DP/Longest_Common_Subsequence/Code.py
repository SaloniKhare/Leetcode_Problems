# ==================================================
# LONGEST COMMON SUBSEQUENCE - ALL APPROACHES
# ==================================================

# Problem:
# Given two strings text1 and text2,
# return the length of their longest common subsequence.


# -------------------------------------------------
# 1️⃣ Brute Force Recursion
# -------------------------------------------------
class RecursionSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + helper(i + 1, j + 1)
            else:
                return max(helper(i + 1, j),
                           helper(i, j + 1))

        return helper(0, 0)


# -------------------------------------------------
# 2️⃣ Memoization (Top Down DP)
# -------------------------------------------------
class MemoizationSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + helper(i + 1, j + 1)
            else:
                memo[(i, j)] = max(helper(i + 1, j),
                                   helper(i, j + 1))

            return memo[(i, j)]

        return helper(0, 0)


# -------------------------------------------------
# 3️⃣ Tabulation (Bottom Up DP)
# -------------------------------------------------
class TabulationSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j],
                                   dp[i][j - 1])

        return dp[m][n]


# -------------------------------------------------
# 4️⃣ Space Optimized (2 Rows)
# -------------------------------------------------
class SpaceOptimizedSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        return prev[n]


# -------------------------------------------------
# 5️⃣ Fully Space Optimized (1D DP)
# -------------------------------------------------
class OneDimensionalSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev_diag = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = 1 + prev_diag
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev_diag = temp

        return dp[n]

