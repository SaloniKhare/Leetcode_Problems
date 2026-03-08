# ======================================================
# MAXIMUM SUBARRAY (KADANE'S PROBLEM) - ALL APPROACHES
# ======================================================

# Problem:
# Given an integer array nums,
# find the contiguous subarray with the largest sum.


# ------------------------------------------------------
# 1️⃣ Brute Force (Triple Loop)
# ------------------------------------------------------

class BruteForceSolution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = float('-inf')

        for i in range(n):
            for j in range(i, n):
                curr = 0
                for k in range(i, j + 1):
                    curr += nums[k]
                max_sum = max(max_sum, curr)

        return max_sum


# ------------------------------------------------------
# 2️⃣ Better Brute Force (Double Loop)
# ------------------------------------------------------

class BetterBruteForceSolution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = float('-inf')

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum


# ------------------------------------------------------
# 3️⃣ Divide and Conquer
# ------------------------------------------------------

class DivideConquerSolution:
    def maxSubArray(self, nums):

        def solve(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            left_sum = solve(left, mid)
            right_sum = solve(mid + 1, right)

            # Cross sum
            curr = 0
            left_cross = float('-inf')
            for i in range(mid, left - 1, -1):
                curr += nums[i]
                left_cross = max(left_cross, curr)

            curr = 0
            right_cross = float('-inf')
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                right_cross = max(right_cross, curr)

            cross_sum = left_cross + right_cross

            return max(left_sum, right_sum, cross_sum)

        return solve(0, len(nums) - 1)


# ------------------------------------------------------
# 4️⃣ Dynamic Programming (Kadane's Algorithm) ⭐
# ------------------------------------------------------

class KadaneSolution:
    def maxSubArray(self, nums):
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


# ------------------------------------------------------
# 5️⃣ DP Array
# ------------------------------------------------------

class DPArraySolution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        max_sum = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            max_sum = max(max_sum, dp[i])

        return max_sum


# ------------------------------------------------------
# 6️⃣ Prefix Sum Method
# ------------------------------------------------------

class PrefixSumSolution:
    def maxSubArray(self, nums):
        prefix = 0
        min_prefix = 0
        max_sum = float('-inf')

        for num in nums:
            prefix += num
            max_sum = max(max_sum, prefix - min_prefix)
            min_prefix = min(min_prefix, prefix)

        return max_sum
