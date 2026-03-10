# ======================================================
# RUSSIAN DOLL ENVELOPES - ALL APPROACHES
# ======================================================

# Problem:
# envelopes[i] = [width, height]
# One envelope can fit into another if:
# w1 < w2 and h1 < h2
# Find the maximum number of envelopes you can nest.


# ------------------------------------------------------
# 1️⃣ Brute Force (Recursion)
# ------------------------------------------------------

class RecursionSolution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort()
        n = len(envelopes)

        def dfs(index, prev):
            if index == n:
                return 0

            take = 0
            if prev == -1 or (
                envelopes[index][0] > envelopes[prev][0] and
                envelopes[index][1] > envelopes[prev][1]
            ):
                take = 1 + dfs(index + 1, index)

            skip = dfs(index + 1, prev)

            return max(take, skip)

        return dfs(0, -1)


# ------------------------------------------------------
# 2️⃣ Memoization (Top-Down DP)
# ------------------------------------------------------

class MemoizationSolution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort()
        n = len(envelopes)
        memo = {}

        def dfs(i, prev):
            if i == n:
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            take = 0
            if prev == -1 or (
                envelopes[i][0] > envelopes[prev][0] and
                envelopes[i][1] > envelopes[prev][1]
            ):
                take = 1 + dfs(i + 1, i)

            skip = dfs(i + 1, prev)

            memo[(i, prev)] = max(take, skip)
            return memo[(i, prev)]

        return dfs(0, -1)


# ------------------------------------------------------
# 3️⃣ DP (LIS O(n²))
# ------------------------------------------------------

class DPLISSolution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort()
        n = len(envelopes)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if (
                    envelopes[j][0] < envelopes[i][0] and
                    envelopes[j][1] < envelopes[i][1]
                ):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# ------------------------------------------------------
# 4️⃣ Optimal Solution (Sort + LIS + Binary Search) ⭐
# ------------------------------------------------------

import bisect

class BinarySearchSolution:
    def maxEnvelopes(self, envelopes):

        # Important trick
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        heights = [h for _, h in envelopes]

        lis = []

        for h in heights:
            pos = bisect.bisect_left(lis, h)

            if pos == len(lis):
                lis.append(h)
            else:
                lis[pos] = h

        return len(lis)


# ------------------------------------------------------
# 5️⃣ Greedy + Patience Sorting (Same as LIS)
# ------------------------------------------------------

class PatienceSortingSolution:
    def maxEnvelopes(self, envelopes):

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        import bisect
        piles = []

        for _, h in envelopes:
            pos = bisect.bisect_left(piles, h)

            if pos == len(piles):
                piles.append(h)
            else:
                piles[pos] = h

        return len(piles)
