# ==========================================
# WORD BREAK - ALL APPROACHES
# ==========================================

# Problem:
# Given a string s and a dictionary of strings wordDict,
# return True if s can be segmented into a space-separated
# sequence of one or more dictionary words.


# -------------------------------------------------
# 1️⃣ Brute Force / Pure Recursion
# -------------------------------------------------
class RecursionSolution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)

        def helper(start):
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet and helper(end):
                    return True

            return False

        return helper(0)


# -------------------------------------------------
# 2️⃣ Memoization (Top Down DP)
# -------------------------------------------------
class MemoizationSolution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def helper(start):
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet and helper(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return helper(0)


# -------------------------------------------------
# 3️⃣ Tabulation (Bottom Up DP)
# -------------------------------------------------
class TabulationSolution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True  # empty string

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]


# -------------------------------------------------
# 4️⃣ Space Optimized (Already Optimal 1D DP)
# -------------------------------------------------
class SpaceOptimizedSolution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        max_len = max(map(len, wordDict)) if wordDict else 0

        for i in range(1, n + 1):
            for l in range(1, min(max_len, i) + 1):
                if dp[i - l] and s[i - l:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]


# -------------------------------------------------
# 5️⃣ BFS Approach
# -------------------------------------------------
from collections import deque

class BFSSolution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        queue = deque([0])
        visited = set()

        while queue:
            start = queue.popleft()

            if start in visited:
                continue
            visited.add(start)

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet:
                    if end == len(s):
                        return True
                    queue.append(end)

        return False
