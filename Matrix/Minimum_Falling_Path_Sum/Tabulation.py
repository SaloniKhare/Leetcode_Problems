``` python
class TabulationSolution:
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        # Copy first row
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, n):
            for j in range(n):
                up = dp[i - 1][j]
                left_diag = dp[i - 1][j - 1] if j > 0 else float('inf')
                right_diag = dp[i - 1][j + 1] if j < n - 1 else float('inf')
                dp[i][j] = matrix[i][j] + min(up, left_diag, right_diag)
        return min(dp[n - 1])
```
