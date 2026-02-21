# ==============================
# HOUSE ROBBER - ALL APPROACHES
# ==============================

# Problem:
# You are given an integer array nums representing the amount of money
# of each house. You cannot rob two adjacent houses.
# Return the maximum amount you can rob.


class RecursionSolution:
    def rob(self, nums):
        def helper(index):
            if index >= len(nums):
                return 0
            # Option 1: Rob this house
            rob_current = nums[index] + helper(index + 2)
            # Option 2: Skip this house
            skip_current = helper(index + 1)
            return max(rob_current, skip_current)
        return helper(0)


class MemoizationSolution:
    def rob(self, nums):
        memo = {}
        def helper(index):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]
            rob_current = nums[index] + helper(index + 2)
            skip_current = helper(index + 1)
            memo[index] = max(rob_current, skip_current)
            return memo[index]
        return helper(0)


class TabulationSolution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[n - 1]


class SpaceOptimizedSolution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        for i in range(2, n):
            current = max(prev1, nums[i] + prev2)
            prev2 = prev1
            prev1 = current
        return prev1
