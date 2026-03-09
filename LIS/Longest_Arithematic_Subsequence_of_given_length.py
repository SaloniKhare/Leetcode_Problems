# ==========================================================
# LONGEST ARITHMETIC SUBSEQUENCE OF GIVEN DIFFERENCE
# ==========================================================

# Problem:
# Given an array arr and an integer difference,
# find the length of the longest subsequence such that
# the difference between adjacent elements equals difference.


# ----------------------------------------------------------
# 1️⃣ Brute Force (Recursion)
# ----------------------------------------------------------

class BruteForceSolution:
    def longestSubsequence(self, arr, difference):
        n = len(arr)

        def dfs(index, prev):
            if index == n:
                return 0

            take = 0
            if prev is None or arr[index] - prev == difference:
                take = 1 + dfs(index + 1, arr[index])

            skip = dfs(index + 1, prev)

            return max(take, skip)

        return dfs(0, None)


# ----------------------------------------------------------
# 2️⃣ Memoization (Top-Down DP)
# ----------------------------------------------------------

class MemoizationSolution:
    def longestSubsequence(self, arr, difference):
        from functools import lru_cache
        n = len(arr)

        @lru_cache(None)
        def dfs(i):
            best = 1
            for j in range(i + 1, n):
                if arr[j] - arr[i] == difference:
                    best = max(best, 1 + dfs(j))
            return best

        ans = 1
        for i in range(n):
            ans = max(ans, dfs(i))

        return ans


# ----------------------------------------------------------
# 3️⃣ Dynamic Programming (Hash Map) ⭐ Optimal
# ----------------------------------------------------------

class DPSolution:
    def longestSubsequence(self, arr, difference):
        dp = {}  # value → longest length ending at this value
        ans = 1

        for num in arr:
            prev = num - difference
            dp[num] = dp.get(prev, 0) + 1
            ans = max(ans, dp[num])

        return ans


# ----------------------------------------------------------
# 4️⃣ Bottom-Up DP (Index Based)
# ----------------------------------------------------------

class DPIndexSolution:
    def longestSubsequence(self, arr, difference):
        n = len(arr)
        dp = [1] * n
        ans = 1

        for i in range(n):
            for j in range(i):
                if arr[i] - arr[j] == difference:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])

        return ans


# ----------------------------------------------------------
# 5️⃣ Using defaultdict
# ----------------------------------------------------------

from collections import defaultdict

class DefaultDictSolution:
    def longestSubsequence(self, arr, difference):
        dp = defaultdict(int)
        ans = 1

        for num in arr:
            dp[num] = dp[num - difference] + 1
            ans = max(ans, dp[num])

        return ans
