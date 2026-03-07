# ============================================================
# LONGEST INCREASING SUBSEQUENCE (LIS) - ALL APPROACHES
# ============================================================

# Problem:
# Given an integer array nums,
# return the length of the longest strictly increasing subsequence.


# ------------------------------------------------------------
# 1️⃣ Brute Force Recursion
# ------------------------------------------------------------

class RecursionSolution:
    def lengthOfLIS(self, nums):
        def dfs(i, prev):
            if i == len(nums):
                return 0

            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + dfs(i + 1, i)

            skip = dfs(i + 1, prev)

            return max(take, skip)

        return dfs(0, -1)


# ------------------------------------------------------------
# 2️⃣ Memoization (Top Down DP)
# ------------------------------------------------------------

class MemoizationSolution:
    def lengthOfLIS(self, nums):
        memo = {}

        def dfs(i, prev):
            if i == len(nums):
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + dfs(i + 1, i)

            skip = dfs(i + 1, prev)

            memo[(i, prev)] = max(take, skip)
            return memo[(i, prev)]

        return dfs(0, -1)


# ------------------------------------------------------------
# 3️⃣ Tabulation DP (Classic O(n²))
# ------------------------------------------------------------

class TabulationSolution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# ------------------------------------------------------------
# 4️⃣ Space Optimized (Same as Tabulation)
# ------------------------------------------------------------
# Already optimized because only 1D DP is needed.


# ------------------------------------------------------------
# 5️⃣ Binary Search + Greedy (Optimal O(n log n))
# ------------------------------------------------------------

import bisect

class BinarySearchSolution:
    def lengthOfLIS(self, nums):
        lis = []

        for num in nums:
            pos = bisect.bisect_left(lis, num)

            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        return len(lis)


# ------------------------------------------------------------
# 6️⃣ Patience Sorting Method
# ------------------------------------------------------------

class PatienceSortingSolution:
    def lengthOfLIS(self, nums):
        piles = []

        for num in nums:
            left, right = 0, len(piles)

            while left < right:
                mid = (left + right) // 2

                if piles[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(piles):
                piles.append(num)
            else:
                piles[left] = num

        return len(piles)
