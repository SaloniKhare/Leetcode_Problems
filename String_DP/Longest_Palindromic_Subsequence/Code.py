# ==========================================================
# LONGEST PALINDROMIC SUBSEQUENCE - ALL 6 APPROACHES
# ==========================================================

# Problem:
# Given a string s, return the length of the longest palindromic subsequence.


# -------------------------------------------------
# 1️⃣ Brute Force Recursion
# -------------------------------------------------
class RecursionSolution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def helper(l, r):
            if l > r:
                return 0
            if l == r:
                return 1

            if s[l] == s[r]:
                return 2 + helper(l + 1, r - 1)
            else:
                return max(helper(l + 1, r), helper(l, r - 1))

        return helper(0, len(s) - 1)


# -------------------------------------------------
# 2️⃣ Memoization (Top Down DP)
# -------------------------------------------------
class MemoizationSolution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}

        def helper(l, r):
            if l > r:
                return 0
            if l == r:
                return 1

            if (l, r) in memo:
                return memo[(l, r)]

            if s[l] == s[r]:
                memo[(l, r)] = 2 + helper(l + 1, r - 1)
            else:
                memo[(l, r)] = max(helper(l + 1, r),
                                   helper(l, r - 1))

            return memo[(l, r)]

        return helper(0, len(s) - 1)


# -------------------------------------------------
# 3️⃣ Tabulation (Bottom Up DP)
# -------------------------------------------------
class TabulationSolution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] if length > 2 else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


# -------------------------------------------------
# 4️⃣ Space Optimized DP (1D)
# -------------------------------------------------
class SpaceOptimizedSolution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            prev = 0
            dp[i] = 1
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = 2 + prev
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return dp[n - 1]


# -------------------------------------------------
# 5️⃣ Using LCS (Reverse String Trick)
# -------------------------------------------------
class LCSSolution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        n = len(s)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][n]


# -------------------------------------------------
# 6️⃣ Space Optimized LCS (1D DP)
# -------------------------------------------------
class SpaceOptimizedLCSSolution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        n = len(s)

        prev = [0] * (n + 1)

        for i in range(1, n + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        return prev[n]
