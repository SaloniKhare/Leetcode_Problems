```python
# ==============================
# CLIMBING STAIRS - ALL APPROACHES
# ==============================

class RecursionSolution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class MemoizationSolution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(n):
            if n <= 2:
                return n
            if n in memo:
                return memo[n]
            memo[n] = dp(n - 1) + dp(n - 2)
            return memo[n]

        return dp(n)


class TabulationSolution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


class SpaceOptimizedSolution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev2 = 1
        prev1 = 2

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1
```
