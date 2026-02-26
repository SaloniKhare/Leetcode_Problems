``` python
class MemoizationSolution:
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        memo = {}
        def helper(i, j):
            if j < 0 or j >= n:
                return float('inf')
            if i == n - 1:
                return matrix[i][j]
            if (i, j) in memo:
                return memo[(i, j)]
            down = helper(i + 1, j)
            left_diag = helper(i + 1, j - 1)
            right_diag = helper(i + 1, j + 1)
            memo[(i, j)] = matrix[i][j] + min(down, left_diag, right_diag)
            return memo[(i, j)]
        result = float('inf')
        for col in range(n):
            result = min(result, helper(0, col))
        return result
```
