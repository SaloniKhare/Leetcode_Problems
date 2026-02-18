# ==============================
# TRIBONACCI NUMBER - ALL APPROACHES
# ==============================

# --------------------------------------------------
# Recursive Approach (Brute Force)
# Time Complexity: O(3^n)
# Space Complexity: O(n)
# --------------------------------------------------

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        return (
            self.tribonacci(n - 1) +
            self.tribonacci(n - 2) +
            self.tribonacci(n - 3)
        )

# --------------------------------------------------
# Recursion + Memoization (Top-Down DP)
# Time Complexity: O(n)
# Space Complexity: O(n)
# --------------------------------------------------

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def solve(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n in memo:
                return memo[n]

            memo[n] = (
                solve(n - 1) +
                solve(n - 2) +
                solve(n - 3)
            )
            return memo[n]

        return solve(n)

# --------------------------------------------------
# Tabulation (Bottom-Up DP)
# Time Complexity: O(n)
# Space Complexity: O(n)
# --------------------------------------------------

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]

# --------------------------------------------------
# Space Optimized DP
# Time Complexity: O(n)
# Space Complexity: O(1)
# --------------------------------------------------

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        prev3 = 0   # T0
        prev2 = 1   # T1
        prev1 = 1   # T2

        for _ in range(3, n + 1):
            current = prev1 + prev2 + prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = current

        return prev1
