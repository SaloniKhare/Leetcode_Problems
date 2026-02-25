``` python
class TabulationSolution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [[0] * len(row) for row in triangle]
        # Copy last row
        dp[n - 1] = triangle[n - 1][:]
        # Build from bottom to top
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(
                    dp[i + 1][j],
                    dp[i + 1][j + 1]
                )
        return dp[0][0]
```
