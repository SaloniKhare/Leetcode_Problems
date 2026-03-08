# ======================================================
# MAXIMUM LENGTH OF PAIR CHAIN - ALL APPROACHES
# ======================================================

# Problem:
# pairs[i] = [a, b]
# A pair (c, d) can follow (a, b) if b < c
# Find the longest chain possible.


# ------------------------------------------------------
# 1️⃣ Brute Force (Recursion)
# ------------------------------------------------------

class BruteForceSolution:
    def findLongestChain(self, pairs):
        pairs.sort()

        def dfs(index, prev_end):
            if index == len(pairs):
                return 0

            take = 0
            if pairs[index][0] > prev_end:
                take = 1 + dfs(index + 1, pairs[index][1])

            skip = dfs(index + 1, prev_end)

            return max(take, skip)

        return dfs(0, float('-inf'))


# ------------------------------------------------------
# 2️⃣ Memoization (Top-Down DP)
# ------------------------------------------------------

class MemoizationSolution:
    def findLongestChain(self, pairs):
        pairs.sort()
        memo = {}

        def dfs(i, prev):
            if i == len(pairs):
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            take = 0
            if pairs[i][0] > prev:
                take = 1 + dfs(i + 1, pairs[i][1])

            skip = dfs(i + 1, prev)

            memo[(i, prev)] = max(take, skip)
            return memo[(i, prev)]

        return dfs(0, float('-inf'))


# ------------------------------------------------------
# 3️⃣ DP (Longest Increasing Subsequence Style)
# ------------------------------------------------------

class DPLISSolution:
    def findLongestChain(self, pairs):
        pairs.sort()
        n = len(pairs)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# ------------------------------------------------------
# 4️⃣ Greedy (Optimal Approach) ⭐
# ------------------------------------------------------

class GreedySolution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])  # sort by end time

        curr_end = float('-inf')
        count = 0

        for start, end in pairs:
            if start > curr_end:
                count += 1
                curr_end = end

        return count


# ------------------------------------------------------
# 5️⃣ Binary Search (LIS Optimization Idea)
# ------------------------------------------------------

import bisect

class BinarySearchSolution:
    def findLongestChain(self, pairs):
        pairs.sort()
        dp = []

        for start, end in pairs:
            pos = bisect.bisect_left(dp, start)

            if pos == len(dp):
                dp.append(end)
            else:
                dp[pos] = min(dp[pos], end)

        return len(dp)
